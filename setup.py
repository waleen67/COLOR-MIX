from setuptools import setup, find_packages

setup(
    name="color-mixer",
    version="1.0.0",
    author="Your Name",
    description="A simple color mixing simulator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["color_mixer"],
    entry_points={
        "console_scripts": [
            "color-mixer=color_mixer:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
