from setuptools import setup, find_packages

setup(
    name = "ch2",
    version = 1.0,
    description = "GA codes of chapter 2",
    packages = find_packages(),
    entry_points=
    """
    [console_scripts]
    ch2run = ch2.population:main
    """,
)

