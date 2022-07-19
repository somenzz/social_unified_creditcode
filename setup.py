from pathlib import Path

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    raise ImportError(
        'Could not import "setuptools".' "Please install the setuptools package."
    )


readme = Path("README.md")
license = Path("LICENSE")


# Read the version without importing the package
# (and thus attempting to import packages it depends on that may not be
# installed yet)
version = "0.1"

NAME = "succ_utils"
VERSION = version
DESCRIPTION = "统一社会信用代码校验，生成"
KEYWORDS = "social unified credit code, 统一社会信用代码校验，生成"
AUTHOR = "somenzz"
AUTHOR_EMAIL = "somenzz@163.com"
URL = "https://github.com/somenzz/social_unified_creditcode"
LICENSE = license.read_text()
PACKAGES = find_packages(exclude=["tests", "test.*"])
print(PACKAGES)

INSTALL_REQUIRES = []
TEST_SUITE = "tests"
TESTS_REQUIRE = []

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
]

LONG_DESCRIPTION = readme


params = {
    "name": NAME,
    "version": VERSION,
    "description": DESCRIPTION,
    "keywords": KEYWORDS,
    "author": AUTHOR,
    "author_email": AUTHOR_EMAIL,
    "url": URL,
    "packages": PACKAGES,
    "license": "MIT",
    "install_requires": INSTALL_REQUIRES,
    "tests_require": TESTS_REQUIRE,
    "test_suite": TEST_SUITE,
    "classifiers": CLASSIFIERS,
    "long_description": readme.read_text(),
}

if __name__ == "__main__":
    setup(**params, long_description_content_type="text/markdown")
