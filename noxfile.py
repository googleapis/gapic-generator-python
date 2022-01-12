# Copyright 2017, Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import os
import sys
import tempfile
import typing
import nox  # type: ignore

from contextlib import contextmanager
from os import path
import shutil


showcase_version = os.environ.get("SHOWCASE_VERSION", "0.18.0")
ADS_TEMPLATES = path.join(path.dirname(__file__), "gapic", "ads-templates")


ALL_PYTHON = (
    "3.6",
    "3.7",
    "3.8",
    "3.9",
)

NEWEST_PYTHON = "3.9"


@nox.session(python=ALL_PYTHON)
def unit(session):
    """Run the unit test suite."""

    session.install(
        "coverage", "pytest-cov", "pytest", "pytest-xdist", "pyfakefs", "grpcio-status",
    )
    session.install("-e", ".")

    session.run(
        "py.test",
        *(
            session.posargs
            or [
                "-vv",
                "-n=auto",
                "--cov=gapic",
                "--cov-config=.coveragerc",
                "--cov-report=term",
                "--cov-fail-under=100",
                path.join("tests", "unit"),
            ]
        ),
    )


FRAG_DIR = Path("tests") / "fragments"
FRAGMENT_FILES = tuple(
    Path(dirname).relative_to(FRAG_DIR) / f
    for dirname, _, files in os.walk(FRAG_DIR)
    for f in files
    if os.path.splitext(f)[1] == ".proto" and f.startswith("test_")
)

# Note: this class lives outside 'fragment'
# so that, if necessary, it can be pickled for a ProcessPoolExecutor
# A callable class is necessary so that the session can be closed over
# instead of passed in, which simplifies the invocation via map.
class FragTester:
    def __init__(self, session, use_ads_templates):
        self.session = session
        self.use_ads_templates = use_ads_templates

    def __call__(self, frag):
        with tempfile.TemporaryDirectory() as tmp_dir:
            # Generate the fragment GAPIC.
            outputs = []
            templates = (
                path.join(path.dirname(__file__), "gapic", "ads-templates")
                if self.use_ads_templates
                else "DEFAULT"
            )
            maybe_old_naming = ",old-naming" if self.use_ads_templates else ""

            session_args = [
                "python",
                "-m",
                "grpc_tools.protoc",
                f"--proto_path={str(FRAG_DIR)}",
                f"--python_gapic_out={tmp_dir}",
                f"--python_gapic_opt=transport=grpc+rest,python-gapic-templates={templates}{maybe_old_naming}",
            ]

            outputs.append(
                self.session.run(*session_args, str(frag), external=True, silent=True,)
            )

            # Install the generated fragment library.
            # Note: install into the tempdir to prevent issues
            # with running pip concurrently.
            self.session.install(tmp_dir, "-e", ".", "-t", tmp_dir, "-qqq")
            # Run the fragment's generated unit tests.
            # Don't bother parallelizing them: we already parallelize
            # the fragments, and there usually aren't too many tests per fragment.
            outputs.append(
                self.session.run(
                    "py.test",
                    "--quiet",
                    f"--cov-config={str(Path(tmp_dir) / '.coveragerc')}",
                    "--cov-report=term",
                    "--cov-fail-under=100",
                    str(Path(tmp_dir) / "tests" / "unit"),
                    silent=True,
                )
            )

            return "".join(outputs)


# TODO(dovs): ads templates
@nox.session(python=ALL_PYTHON)
def fragment(session):
    session.install(
        "coverage",
        "pytest",
        "pytest-cov",
        "pytest-xdist",
        "asyncmock",
        "pytest-asyncio",
        "grpcio-tools",
    )
    session.install("-e", ".")

    with ThreadPoolExecutor() as p:
        all_outs = p.map(FragTester(session, False), FRAGMENT_FILES)

    output = "".join(all_outs)
    session.log(output)


@nox.session(python=ALL_PYTHON[1:])
def fragment_alternative_templates(session):
    session.install(
        "coverage",
        "pytest",
        "pytest-cov",
        "pytest-xdist",
        "asyncmock",
        "pytest-asyncio",
        "grpcio-tools",
    )
    session.install("-e", ".")

    with ThreadPoolExecutor() as p:
        all_outs = p.map(FragTester(session, True), FRAGMENT_FILES)

    output = "".join(all_outs)
    session.log(output)


# TODO(yon-mg): -add compute context manager that includes rest transport
#               -add compute unit tests
#               (to test against temporarily while rest transport is incomplete)
#               (to be removed once all features are complete)
@contextmanager
def showcase_library(
    session, templates="DEFAULT", other_opts: typing.Iterable[str] = ()
):
    """Install the generated library into the session for showcase tests."""

    # Try to make it clear if Showcase is not running, so that
    # people do not end up with tons of difficult-to-debug failures over
    # an obvious problem.
    if not os.environ.get("CIRCLECI"):
        session.log("-" * 70)
        session.log("Note: Showcase must be running for these tests to work.")
        session.log("See https://github.com/googleapis/gapic-showcase")
        session.log("-" * 70)

    # Install gapic-generator-python
    session.install("-e", ".")

    # Install grpcio-tools for protoc
    session.install("grpcio-tools")

    # Install a client library for Showcase.
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Download the Showcase descriptor.
        session.run(
            "curl",
            "https://github.com/googleapis/gapic-showcase/releases/"
            f"download/v{showcase_version}/"
            f"gapic-showcase-{showcase_version}.desc",
            "-L",
            "--output",
            path.join(tmp_dir, "showcase.desc"),
            external=True,
            silent=True,
        )

        # Write out a client library for Showcase.
        template_opt = f"python-gapic-templates={templates}"
        opts = "--python_gapic_opt="
        opts += ",".join(other_opts + (f"{template_opt}", "transport=grpc+rest"))
        cmd_tup = (
            "python",
            "-m",
            "grpc_tools.protoc",
            f"--experimental_allow_proto3_optional",
            f"--descriptor_set_in={tmp_dir}{path.sep}showcase.desc",
            opts,
            f"--python_gapic_out={tmp_dir}",
            f"google/showcase/v1beta1/echo.proto",
            f"google/showcase/v1beta1/identity.proto",
            f"google/showcase/v1beta1/messaging.proto",
        )
        session.run(
            *cmd_tup, external=True,
        )

        # Install the library.
        session.install("-e", tmp_dir)

        yield tmp_dir


@nox.session(python=NEWEST_PYTHON)
def showcase(
    session,
    templates="DEFAULT",
    other_opts: typing.Iterable[str] = (),
    env: typing.Optional[typing.Dict[str, str]] = None,
):
    """Run the Showcase test suite."""

    with showcase_library(session, templates=templates, other_opts=other_opts):
        session.install("mock", "pytest", "pytest-asyncio")
        session.run(
            "py.test",
            "--quiet",
            *(session.posargs or [path.join("tests", "system")]),
            env=env,
        )


@nox.session(python=NEWEST_PYTHON)
def showcase_mtls(
    session,
    templates="DEFAULT",
    other_opts: typing.Iterable[str] = (),
    env: typing.Optional[typing.Dict[str, str]] = None,
):
    """Run the Showcase mtls test suite."""

    with showcase_library(session, templates=templates, other_opts=other_opts):
        session.install("mock", "pytest", "pytest-asyncio")
        session.run(
            "py.test",
            "--quiet",
            "--mtls",
            *(session.posargs or [path.join("tests", "system")]),
            env=env,
        )


@nox.session(python=NEWEST_PYTHON)
def showcase_alternative_templates(session):
    templates = path.join(path.dirname(__file__), "gapic", "ads-templates")
    showcase(
        session,
        templates=templates,
        other_opts=("old-naming",),
        env={"GAPIC_PYTHON_ASYNC": "False"},
    )


@nox.session(python=NEWEST_PYTHON)
def showcase_mtls_alternative_templates(session):
    templates = path.join(path.dirname(__file__), "gapic", "ads-templates")
    showcase_mtls(
        session,
        templates=templates,
        other_opts=("old-naming",),
        env={"GAPIC_PYTHON_ASYNC": "False"},
    )


def run_showcase_unit_tests(session, fail_under=100):
    session.install(
        "coverage",
        "pytest",
        "pytest-cov",
        "pytest-xdist",
        "asyncmock",
        "pytest-asyncio",
    )

    # Run the tests.
    session.run(
        "py.test",
        "-n=auto",
        "--quiet",
        "--cov=google",
        "--cov-append",
        f"--cov-fail-under={str(fail_under)}",
        *(session.posargs or [path.join("tests", "unit")]),
    )


@nox.session(python=ALL_PYTHON)
def showcase_unit(
    session, templates="DEFAULT", other_opts: typing.Iterable[str] = (),
):
    """Run the generated unit tests against the Showcase library."""

    with showcase_library(session, templates=templates, other_opts=other_opts) as lib:
        session.chdir(lib)
        run_showcase_unit_tests(session)


@nox.session(python=ALL_PYTHON[1:])  # Do not test 3.6
def showcase_unit_alternative_templates(session):
    with showcase_library(
        session, templates=ADS_TEMPLATES, other_opts=("old-naming",)
    ) as lib:
        session.chdir(lib)
        run_showcase_unit_tests(session)


@nox.session(python=NEWEST_PYTHON)
def showcase_unit_add_iam_methods(session):
    with showcase_library(session, other_opts=("add-iam-methods",)) as lib:
        session.chdir(lib)

        # Unit tests are run twice with different dependencies.
        # 1. Run tests at lower bound of dependencies.
        session.install("nox")
        session.run("nox", "-s", "update_lower_bounds")
        session.install(".", "--force-reinstall", "-c", "constraints.txt")
        run_showcase_unit_tests(session, fail_under=0)

        # 2. Run the tests again with latest version of dependencies.
        session.install(".", "--upgrade", "--force-reinstall")
        run_showcase_unit_tests(session, fail_under=100)


@nox.session(python=NEWEST_PYTHON)
def showcase_mypy(
    session, templates="DEFAULT", other_opts: typing.Iterable[str] = (),
):
    """Perform typecheck analysis on the generated Showcase library."""

    # Install pytest and gapic-generator-python
    session.install("mypy", "types-pkg-resources")

    with showcase_library(session, templates=templates, other_opts=other_opts) as lib:
        session.chdir(lib)

        # Run the tests.
        session.run("mypy", "--explicit-package-bases", "google")


@nox.session(python=NEWEST_PYTHON)
def showcase_mypy_alternative_templates(session):
    showcase_mypy(session, templates=ADS_TEMPLATES, other_opts=("old-naming",))


@nox.session(python=NEWEST_PYTHON)
def snippetgen(session):
    # Clone googleapis/api-common-protos which are referenced by the snippet
    # protos
    api_common_protos = "api-common-protos"
    try:
        session.run("git", "-C", api_common_protos, "pull", external=True)
    except nox.command.CommandFailed:
        session.run(
            "git",
            "clone",
            "--single-branch",
            f"https://github.com/googleapis/{api_common_protos}",
            external=True,
        )

    # Install gapic-generator-python
    session.install("-e", ".")

    session.install("grpcio-tools", "mock", "pytest", "pytest-asyncio")

    session.run("py.test", "-vv", "tests/snippetgen")


@nox.session(python=NEWEST_PYTHON)
def docs(session):
    """Build the docs."""

    session.install("sphinx < 1.8", "sphinx_rtd_theme")
    session.install(".")

    # Build the docs!
    session.run("rm", "-rf", "docs/_build/")
    session.run(
        "sphinx-build",
        "-W",
        "-b",
        "html",
        "-d",
        "docs/_build/doctrees",
        "docs/",
        "docs/_build/html/",
    )


@nox.session(python=NEWEST_PYTHON)
def mypy(session):
    """Perform typecheck analysis."""

    session.install("mypy", "types-protobuf", "types-PyYAML", "types-dataclasses")
    session.install(".")
    session.run("mypy", "gapic")
