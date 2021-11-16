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
    name="oauth_toolkit_extensions",
    sources=[
      "**/*.py",
    ],
    dependencies=[":mitol-django-common", ":files"],
)

python_distribution(
    name="mitol-django-oauth-toolkit-extensions",
    dependencies=[":oauth_toolkit_extensions"],
    provides=setup_py(
        name="mitol-django-oauth-toolkit-extensions",
        description="MIT Open Learning django app extensions for oauth toolkit",
    ),
    setup_py_commands=["sdist", "bdist_wheel"]
)
