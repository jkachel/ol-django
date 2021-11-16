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

python_requirement_library(
    name="mitol-django-maail",
    requirements=["mitol-django-mail~=3.0"],
    module_mapping={
        "mitol-django-mail": ["mitol.mail"]
    }
)

python_library(
    name="authentication",
    sources=[
        "**/*.py",
    ],
    dependencies=[
        ":mitol-django-common",
        ":files",
    ],
)

python_distribution(
    name="mitol-django-authentication",
    dependencies=[":authentication"],
    provides=setup_py(
        name="mitol-django-authentication",
        description="MIT Open Learning django app extensions for oauth toolkit",
    ),
    setup_py_commands=["sdist", "bdist_wheel"]
)
