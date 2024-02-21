from setuptools import setup, find_packages


def main():
    """
    Uses setuptools to build the python library based on python code and handles the installation of requirements
    from a requirements.txt file.
    :return:
    """
    with open("requirements.txt", "r") as f:
        requirements = f.read().splitlines()

    setup(
        name="EkonsBase",
        version="0.0.1",
        description="Ekons Scheduler",
        author="BCG",
        install_requires=requirements,
        packages=find_packages(),
        package_data={
            "EkonsBase": ["docs/*", "docs/**/**", "config/*", "config/**/**"]
        },
        entry_points={
            "console_scripts": ["ekons-cli=EkonsBase.entrypoints.entrypoints:cli"]
        },
    )


if __name__ == "__main__":
    main()
