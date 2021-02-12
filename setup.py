from setuptools import setup

with open("README.md", encoding="utf-8") as f:
	long_description = f.read()

setup(
	name="pixelpainter",
	version="0.3",
	description="Convert images to HTML.",
	long_description = long_description,
	long_description_content_type="text/markdown",
	author="Pedro Torcatt",
	author_email="pedrotorcattsoto@gmail.com",
	url="https://github.com/Jalkhov/pixelpainter",
	license = "MIT",
	keywords = "paint html pixel convert image",
	packages=['pixelpainter'],
	install_requires=[
		'numpy',
		'pyperclip'
	],
	entry_points={
		'console_scripts': [
			'pixelpainter = pixelpainter.main:main',
		],
	},
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Environment :: Console",
		"Operating System :: Microsoft :: Windows",
		"Programming Language :: Python :: 3",
		"Topic :: Utilities",
		"Topic :: Scientific/Engineering :: Image Processing",
		"License :: OSI Approved :: MIT License",
	],
)