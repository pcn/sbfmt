# Based on the google/gcr distroless repo, get package lists from debian snapshot
# package repos, and pull packages from there

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

git_repository(
    name = "io_bazel_rules_python",
    # remote = "https://github.com/bazelbuild/rules_python.git",
    # commit = "44711d8ef543f6232aec8445fb5adce9a04767f9"
    # Temporarily leaving bazelbuild for ali5h. This repo deals with
    # https://github.com/bazelbuild/rules_python/pull/90 but this
    # particular repo+branch seems to fix our problems with less code.
    # So until bazel merges the above, let's use this branch, which
    # uses ali5h's fixes, but merged with more recent upstream changes.
    remote = "https://github.com/pcn/rules_python.git",
    commit = "d0205c2581932f95368cac3c5e44ac4b0797254e",
    # commit = "d9afd32286c9e61b8ca95c9218523a3b64aea709",
    shallow_since = "1558035897 -0400"    
)


# Needed for PIP support:
load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories")

pip_repositories()

load("@io_bazel_rules_python//python:pip.bzl", "pip_import")

# For each python project that has its own requirements.txt, read it in
# and turn each pypi package and its dependencies into requirements
# that bazel can consume in BUILD files.

pip_import(
    name = "sbfmt_deps",
    requirements = "//sbfmt:requirements.txt",
)

load(
    "@sbfmt_deps//:requirements.bzl",
    _sbfmt_deps_install="pip_install"
    )
_ops_aws_deps_install()

