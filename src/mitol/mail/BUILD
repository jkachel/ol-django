resources(
  name="mail-templates",
  sources=["templates/**/*"]
)

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
    name="mail",
    sources=[
      "**/*.py",
    ],
    dependencies=[
        ":mitol-django-common",
        ":mail-templates",
        ":files",
        "//:html5lib",  # pulled in dynamically by bs4
    ],
)

python_distribution(
    name="mitol-django-mail",
    dependencies=[":mail"],
    provides=setup_py(
        name="mitol-django-mail",
        description="MIT Open Learning django app extensions for mail",
    ),
    setup_py_commands=["sdist", "bdist_wheel"]
)
