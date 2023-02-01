from setuptools import find_packages, setup

setup(
    name="PGB",
    packages=find_packages(include=["PGB"]),
    version="0.1.0",
    description="A pygame wrapper.",
    author="MrCatNerd#0669",
    license="MIT",
    install_requires=["pygame"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
