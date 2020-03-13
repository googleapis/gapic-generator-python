load("@rules_python//python:pip.bzl", "pip_import")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

def com_google_protoc_java_resource_names_plugin_repositories():
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
        sha256 = "bbccf674aa441c266df9894182d80de104cabd19be98be002f6d478aaa31574d",
        strip_prefix = "bazel-skylib-2169ae1c374aab4a09aa90e65efe1a3aad4e279b",
        urls = ["https://github.com/bazelbuild/bazel-skylib/archive/2169ae1c374aab4a09aa90e65efe1a3aad4e279b.tar.gz"],
    )


    pip_import(
        name = "examples_helloworld",
        requirements = "@rules_python//examples/helloworld:requirements.txt",
    )


def _maybe(repo_rule, name, strip_repo_prefix = "", **kwargs):
    if not name.startswith(strip_repo_prefix):
        return
    repo_name = name[len(strip_repo_prefix):]
    if repo_name in native.existing_rules():
        return
    repo_rule(name = repo_name, **kwargs)
