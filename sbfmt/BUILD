# Bazel build targets

package(default_visibility = ["//visibility:public"])

# Create build info
genrule(
  name = "genpybuildinfo",
  outs = [
    "buildinfo.py",
  ],
  stamp = 1,
  cmd = "./$(location tools/mkpybuildinfo.sh) > \"$@\"",
  tools = [
    "tools/mkpybuildinfo.sh",
  ],
)

py_library(
  name = "buildinfo",
  srcs = [
    ":genpybuildinfo",
  ],
)


load(
  "@io_bazel_rules_python//python:python.bzl",
  "py_binary", "py_library", "py_test"
)

# Load the pip_install symbol for my_deps, and create the dependencies'
# repositories.

load("@sbfmt_deps//:requirements.bzl", "requirement")

DEPS = [
        requirement("jsonschema"),
        ":buildinfo"        
    ]


py_library(
    name = "ops_aws",
    srcs = glob(["*.py", "**/*.py", "**/version"], exclude=["tests/**", "test*", "build", "setup.py"]),
    deps = DEPS
)

TEST_DEPS = [
    requirement('pytest'),
    requirement('pytest-mock'),
    ":sbfmt"
]

py_test(
    name = "test-run",
    srcs = glob(["tests/**", "test*.py"], exclude=["**/*.pyc", "**/*~", "**/*#", "**/*.json"]),
    deps = DEPS + TEST_DEPS
)
