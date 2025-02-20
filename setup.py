import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='DreamPuppets',
    version='1.0',
    scripts=['generate_requirements.py'],
    packages=setuptools.find_packages(),
    url='https://github.com/OmegaPrimej/DreamPuppets',
    license='MIT',
    author='OMEGA PRIME',
    author_email='OMEGADELTAPRIME78@gmail.com',
    description='Generate interactive digital puppets using AI',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['dream puppets', 'ai', 'interactive', 'digital'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'torch==1.12.1+cu113',
        'transformers==4.22.2',
        'diffusers==0.10.2',
        'replicate-api==1.0.5',
        'ffmpeg-python==0.2.0',
        'SpeechRecognition==3.8.1',
        'pydub==0.25.1',
        'numpy==1.23.1',
        'Pillow==9.3.0',
        'scipy==1.9.1',
    ],
    python_requires='>=3.8',
    include_package_data=True
)
