from setuptools import setup, find_packages

setup(
    name="skills",
    version="0.1.0",
    description="A short description of your project.",
    author="tijuks",
    packages=find_packages(),
    install_requires=[
        # List your runtime dependencies here, for example:
        # "numpy>=1.23.0",
    ],
    python_requires=">=3.7",
    # If you use entry points (CLIs), add them here:
    # entry_points={
    #     'console_scripts': [
    #         'mycli = skills.cli:main',
    #     ],
    # },
)