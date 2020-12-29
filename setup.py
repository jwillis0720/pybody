"""The setup script."""
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test


with open("README.md") as readme_file:
    readme = readme_file.read()
requirements = open("requirements.txt").readlines()


# From https://stackoverflow.com/questions/45150304/how-to-force-a-python-wheel-to-be-platform-specific-when-building-it
# Tell bdsit wheel to be platform specific even though we arent compiling
try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False


except ImportError:
    bdist_wheel = None


class PyTest(test):
    """Define what happens when we run python setup.py test"""

    def initialize_options(self):
        test.initialize_options(self)
        self.pytest_args = "tests/"

    def run_tests(self):
        # Import here, because outside the eggs aren't loaded
        # import shlex
        import pytest

        err_number = pytest.main(["-vvv"])
        sys.exit(err_number)


setup(
    name="sadie",
    version="0.1.0",
    python_requires=">=3.6",
    description="sadie: The Complete Antibody Library",
    author="Jordan R Willis",
    author_email="jwillis0720@gmail.com",
    url="https://github.com/jwillis0720/",
    packages=find_packages(include=["sadie*"], exclude=["tests*", "docs"]),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords=["airr", "annotating", "antibodies"],
    entry_points={
        "console_scripts": [
            "airr=sadie.airr.app:run_airr",
            "make-reference=sadie.reference.app:make_igblast_reference",
            "make-genebank=sadie.reference.app:make_genebank_files_from_dbma",
        ]
    },
    test_suite="tests",
    cmdclass={"tests": PyTest, "bdist_wheel": bdist_wheel},
)
