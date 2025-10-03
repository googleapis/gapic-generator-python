load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

def gapic_generator_python():

    _maybe(
        http_archive,
        name = "bazel_skylib",
        strip_prefix = "bazel-skylib-2169ae1c374aab4a09aa90e65efe1a3aad4e279b",
        urls = ["https://github.com/bazelbuild/bazel-skylib/archive/2169ae1c374aab4a09aa90e65efe1a3aad4e279b.tar.gz"],
    )

    _grpc_version = "1.47.0"
    _grpc_sha256 = "edf25f4db6c841853b7a29d61b0980b516dc31a1b6cdc399bcf24c1446a4a249"
    _maybe(
        http_archive,
        name = "com_github_grpc_grpc",
        sha256 = _grpc_sha256,
        strip_prefix = "grpc-{}".format(_grpc_version),
        url = "https://github.com/grpc/grpc/archive/v{}.zip".format(_grpc_version),
    )
    _rules_gapic_version = "0.5.4"
    _maybe(
        http_archive,
        name = "rules_gapic",
        strip_prefix = "rules_gapic-%s" % _rules_gapic_version,
        urls = ["https://github.com/googleapis/rules_gapic/archive/v%s.tar.gz" % _rules_gapic_version],
    )
    _commit_sha = "fae3e6e091418d6343902debaf545cfc8f32c3ff"
    _maybe(
        http_archive,
        name = "com_google_googleapis",
        strip_prefix = "googleapis-{}".format(_commit_sha),
        urls = ["https://github.com/googleapis/googleapis/archive/{}.zip".format(_commit_sha)],
    )


def _maybe(repo_rule, name, strip_repo_prefix = "", **kwargs):
    if not name.startswith(strip_repo_prefix):
        return
    repo_name = name[len(strip_repo_prefix):]
    if repo_name in native.existing_rules():
        return
    repo_rule(name = repo_name, **kwargs)
