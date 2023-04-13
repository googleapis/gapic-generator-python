workspace(name = "gapic_generator_python")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

_bazel_skylib_version = "1.4.1"

_bazel_skylib_sha256 = "b8a1527901774180afc798aeb28c4634bdccf19c4d98e7bdd1ce79d1fe9aaad7"

http_archive(
    name = "bazel_skylib",
    sha256 = _bazel_skylib_sha256,
    urls = ["https://github.com/bazelbuild/bazel-skylib/releases/download/{0}/bazel-skylib-{0}.tar.gz".format(_bazel_skylib_version)],
)

load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")

bazel_skylib_workspace()

_io_bazel_rules_go_version = "0.33.0"
http_archive(
    name = "io_bazel_rules_go",
    sha256 = "685052b498b6ddfe562ca7a97736741d87916fe536623afb7da2824c0211c369",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v{0}/rules_go-v{0}.zip".format(_io_bazel_rules_go_version),
        "https://github.com/bazelbuild/rules_go/releases/download/v{0}/rules_go-v{0}.zip".format(_io_bazel_rules_go_version),
    ],
)

_rules_python_version = "0.9.0"

_rules_python_sha256 = "5fa3c738d33acca3b97622a13a741129f67ef43f5fdfcec63b29374cc0574c29"

http_archive(
    name = "rules_python",
    sha256 = _rules_python_sha256,
    strip_prefix = "rules_python-{}".format(_rules_python_version),
    url = "https://github.com/bazelbuild/rules_python/archive/{}.tar.gz".format(_rules_python_version),
)

#
# Import gapic-generator-python specific dependencies
#
load(
    "//:repositories.bzl",
    "gapic_generator_python",
    "gapic_generator_register_toolchains",
)

gapic_generator_python()

gapic_generator_register_toolchains()

load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")

protobuf_deps()

# Import boringssl explicitly to override what gRPC imports as its dependency.
# Boringssl build fails on gcc12 without this fix:
# https://github.com/google/boringssl/commit/8462a367bb57e9524c3d8eca9c62733c63a63cf4,
# which is present only in the newest version of boringssl, not the one imported
# by gRPC. Remove this import once gRPC depends on a newer version.
http_archive(
    name = "boringssl",
    sha256 = "b460f8673f3393e58ce506e9cdde7f2c3b2575b075f214cb819fb57d809f052b",
    strip_prefix = "boringssl-bb41bc007079982da419c0ec3186e510cbcf09d0",
    urls = [
        "https://github.com/google/boringssl/archive/bb41bc007079982da419c0ec3186e510cbcf09d0.zip",
    ],
)

#
# Import grpc as a native bazel dependency. This avoids duplication and also
# speeds up loading phase a lot (otherwise python_rules will be building grpcio
# from sources in a single-core speed, which takes around 5 minutes on a regular
# workstation)
#
load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")

grpc_deps()

load("@build_bazel_rules_apple//apple:repositories.bzl", "apple_rules_dependencies")

apple_rules_dependencies()

load("@build_bazel_apple_support//lib:repositories.bzl", "apple_support_dependencies")

apple_support_dependencies()

load("@com_google_googleapis//:repository_rules.bzl", "switched_rules_by_language")

switched_rules_by_language(
    name = "com_google_googleapis_imports",
    gapic = True,
    grpc = True,
)
