# setup.py - Setup script for packaging the myproject package

from setuptools import setup, find_packages

# Load the long description from the README file (to display on PyPI project page)
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Call setup() to configure the package details
setup(
    name="myproject",  # The name of your package as it will appear on PyPI
    version="0.1.0",   # Package version, follow semantic versioning (major.minor.patch)
    author="Your Name",  # Your name (the package author's name)
    author_email="you@example.com",  # Your contact email
    description="A short description of myproject package",  # Short description (appears on PyPI listing)
    long_description=long_description,  # Long description for PyPI (here we use the README.md content)
    long_description_content_type="text/markdown",  # Content type for long_description (e.g. Markdown)
    url="https://github.com/yourusername/myproject",  # URL for your project (GitHub repo or documentation)
    packages=find_packages(),  # Automatically find all packages inside this project
    classifiers=[
        "Development Status :: 4 - Beta",       # How mature is the project (e.g., Alpha, Beta, Production/Stable)
        "Intended Audience :: Developers",      # Who it's for
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",  # License identifier
        "Programming Language :: Python :: 3",     # Supported Python versions
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        # (You can list multiple versions and other classifiers)
    ],
    python_requires=">=3.6",        # Minimum Python version required
    install_requires=[             # Dependencies that pip will install alongside your package
        "requests>=2.20.0",        # Example: the package needs requests 2.20 or above
    ],
    # entry_points (optional): define console_scripts for command-line executables if needed
    # 'console_scripts': ['myproject-cli = myproject.cli:main']
)

