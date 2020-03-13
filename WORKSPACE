workspace(name = "gapic_generator_python")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/archive/748aa53d7701e71101dfd15d800e100f6ff8e5d1.zip",
    strip_prefix = "rules_python-748aa53d7701e71101dfd15d800e100f6ff8e5d1"
)
load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()

# Only needed if using the packaging rules.
load("@rules_python//python:pip.bzl", "pip_repositories")
pip_repositories()



load("@rules_python//python:pip.bzl", "pip_import")

pip_import(   # or pip3_import
   name = "gapic_generator_python_pip_deps",
   requirements = "@gapic_generator_python//:requirements.txt",
   python_interpreter = "python3",
)

load("@gapic_generator_python_pip_deps//:requirements.bzl", "pip_install")
pip_install()

local_repository(
    name = "com_google_api_codegen",
    path = "/usr/local/google/home/vam/_/projects/github/vam-google/gapic-generator",
)