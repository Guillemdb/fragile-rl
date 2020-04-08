from importlib.machinery import SourceFileLoader
from pathlib import Path

from setuptools import find_packages, setup


version = SourceFileLoader(
    "fragile.version", str(Path(__file__).parent / "fragile" / "version.py"),
).load_module()

with open(Path(__file__).with_name("README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Module-specific dependencies.
extras = {
    "gym": ["atari-py==0.1.1", "plangym>=0.0.7"],
}

# Meta dependency groups.
extras["all"] = [item for group in extras.values() for item in group]

setup(
    name="fragile-rl",
    description="Tools for incorporating fragile to the RLib framework .",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    namespace_packages=["fragile", "fragile.rl"],
    version=version.__version__,
    license="MIT",
    author="Guillem Duran Ballester",
    author_email="guillem@fragile.tech",
    url="https://github.com/FragileTech/fragile-rl",
    download_url="https://github.com/FragileTech/fragile-rl",
    keywords=["reinforcement learning", "artificial intelligence", "monte carlo", "planning"],
    tests_require=["pytest>=5.3.5", "hypothesis>=5.6.0"],
    extras_require=extras,
    install_requires=["ray", "fragile>=0.0.47"],
    package_data={"": ["README.md"]},
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
    ],
)
