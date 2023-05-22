from setuptools import find_packages, setup

setup(
    name="etl_cvetan",
    packages=find_packages(exclude=["etl_cvetan_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
