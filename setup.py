from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "ANN_Deep_Learning_Ops_project"
AUTHOR_USER_NAME = "sheshpalsingh"
SRC_REPO = "ANN_Deep_Learning_Ops_project"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="End-to-End ANN_Deep_Learning_Ops_project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
)

