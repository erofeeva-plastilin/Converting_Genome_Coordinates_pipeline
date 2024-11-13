from setuptools import setup, find_packages

setup(
    name="CoordTransfer",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'coordtransfer=CoordTransfer.coordtransfer:main'
        ],
    },
)
