load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@rules_python//python:pip.bzl", "pip_import")

_PANDOC_BUILD_FILE = """
filegroup(
    name = "pandoc",
    srcs = ["bin/pandoc"],
    visibility = ["//visibility:public"],
)"""

def gapic_generator_python():
    _maybe(
        pip_import,
        name = "gapic_generator_python_pip_deps",
        python_interpreter = "python3",
        requirements = "@gapic_generator_python//:requirements.txt",
    )

    _protobuf_version = "3.11.2"
    _protobuf_version_in_link = "v%s" % _protobuf_version
    _maybe(
        http_archive,
        name = "com_google_protobuf",
        urls = ["https://github.com/protocolbuffers/protobuf/archive/%s.zip" % _protobuf_version_in_link],
        strip_prefix = "protobuf-%s" % _protobuf_version,
    )

    _maybe(
        http_archive,
        name = "bazel_skylib",
        strip_prefix = "bazel-skylib-2169ae1c374aab4a09aa90e65efe1a3aad4e279b",
        urls = ["https://github.com/bazelbuild/bazel-skylib/archive/2169ae1c374aab4a09aa90e65efe1a3aad4e279b.tar.gz"],
    )

    _maybe(
        http_archive,
        name = "com_github_grpc_grpc",
        strip_prefix = "grpc-8347f4753568b5b66e49111c60ae2841278d3f33",  # this is 1.25.0 with fixes
        urls = ["https://github.com/grpc/grpc/archive/8347f4753568b5b66e49111c60ae2841278d3f33.zip"],
    )

    _maybe(
        http_archive,
        name = "pandoc_linux",
        build_file_content = _PANDOC_BUILD_FILE,
        strip_prefix = "pandoc-2.2.1",
        url = "https://github.com/jgm/pandoc/releases/download/2.2.1/pandoc-2.2.1-linux.tar.gz",
    )

    _maybe(
        http_archive,
        name = "pandoc_macOS",
        build_file_content = _PANDOC_BUILD_FILE,
        strip_prefix = "pandoc-2.2.1",
        url = "https://github.com/jgm/pandoc/releases/download/2.2.1/pandoc-2.2.1-macOS.zip",
    )

    _maybe(
        http_archive,
        name = "com_google_api_codegen",
        strip_prefix = "gapic-generator-03abac35ec0716c6f426ffc1532f9a62f1c9e6a2",
        urls = ["https://github.com/googleapis/gapic-generator/archive/03abac35ec0716c6f426ffc1532f9a62f1c9e6a2.zip"],
    )

def gapic_generator_register_toolchains():
    native.register_toolchains(
        "@gapic_generator_python//:pandoc_toolchain_linux",
        "@gapic_generator_python//:pandoc_toolchain_macOS",
    )

def _maybe(repo_rule, name, strip_repo_prefix = "", **kwargs):
    if not name.startswith(strip_repo_prefix):
        return
    repo_name = name[len(strip_repo_prefix):]
    if repo_name in native.existing_rules():
        return
    repo_rule(name = repo_name, **kwargs)
