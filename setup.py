from setuptools import find_packages, setup

setup(
    name="PygameBuiltins",
    packages=find_packages(include=["PygameBuiltins"]),
    version="0.2.0",
    description="A pygame wrapper",
    author="MrCatNerd#0669",
    license="MIT",
    install_requires=["pygame-ce"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
