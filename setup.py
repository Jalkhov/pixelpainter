from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pixelpainter",
    version="0.2",
    description="Convert images to HTML.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Pedro Torcatt",
    author_email="pedrotorcattsoto@gmail.com",
    url="https://github.com/Jalkhov/pixelpainter",
    license="MIT",
    keywords="paint html pixel convert image",
    packages=['pixelpainter'],
    install_requires=[
        'numpy',
        'pyperclip'
    ],
    entry_points={
        'console_scripts': [
            'pixelpainter = pixelpainter.core:main',
        ],
    },
    classifiers=[
        "Topic :: Utilities",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering :: Image Processing",
    ],
)
