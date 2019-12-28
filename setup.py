from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gcloud-service",
    version="0.1.0",
    author="Justin Spahr-Summers",
    author_email="justin@jspahrsummers.com",
    description="Base library for Python microservices running on Google Cloud Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/antequant/gcloud-service",
    packages=find_packages(),
    package_data={"gcloud_service": ["py.typed"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Logging",
        "Topic :: System :: Monitoring",
    ],
    install_requires=[
        "google-cloud-error-reporting ~= 0.33",
        "google-cloud-logging ~= 1.14",
    ],
    keywords="google cloud gcloud microservice service",
)
