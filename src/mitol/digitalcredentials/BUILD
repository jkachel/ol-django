resources(name="files", sources=[
    "CHANGELOG.md",
    "README.md",
    "py.typed",
])

python_requirement_library(
    name="mitol-django-common",
    requirements=["mitol-django-common~=2.1"],
    module_mapping={
        "mitol-django-common": ["mitol.common"]
    }
)

python_library(
    name="digitalcredentials",
    sources=[
      "**/*.py"
    ],
    dependencies=[":mitol-django-common", ":files"]
)

python_distribution(
    name="mitol-django-digital-credentials",
    dependencies=[":digitalcredentials"],
    provides=setup_py(
        name="mitol-django-digital-credentials",
        description="Django application to support digital credentials",
    ),
    setup_py_commands=["sdist", "bdist_wheel"]
)
