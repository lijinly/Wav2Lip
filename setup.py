# setup.py
from setuptools import setup, find_packages

setup(
    name="wav2lip",
    version="0.1.0",
    description="Wav2Lip: Accurately Lip-syncing Videos In The Wild",
    long_description=open("README.md").read() if open("README.md").read() else "Wav2Lip: Learning to Lip-sync Videos In The Wild",
    long_description_content_type="text/markdown",
    author="Rudrabha Mukhopadhyay et al.",
    url="https://github.com/Rudrabha/Wav2Lip",
    packages=find_packages(),
    install_requires=[
        "torch>=1.5.0",
        "torchvision>=0.6.0",
        "numpy>=1.18.0",
        "opencv-python>=4.0.0",
        "scipy>=1.4.0",
        "tqdm>=4.45.0",
        "librosa>=0.7.0",
        "matplotlib>=3.1.0",
        "Pillow>=6.0.0",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Video",
    ],
    entry_points={
        "console_scripts": [
            "wav2lip=wav2lip.inference:main",
        ],
    },
)