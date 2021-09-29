from setuptools import find_packages, setup

with open("./README.md") as readme:
    long_description = readme.read()

setup(
    name="eth_kms_signer",
    version="0.1.0",
    author="Viswanath Kapavarapu",
    author_email="viswanath.iit@gmail.com",
    description="KMS signer for Ethereum",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/viswanathkgp12/eth_kms_signer",
    packages=find_packages(exclude=("tests")),
    package_data={"eth_kms_signer": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    license="MIT",
    zip_safe=False,
    install_requires=[
        "boto3>=1.18.44,<2.0.0",
        "py-ecc>=5.2.0,<6.0.0",
        "ecdsa>=0.17.0,<1.0.0",
        "eth-account>=0.5.5,<1.0.0",
    ],
    python_requires=">=3.5",
)
