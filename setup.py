import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements= [i.strip() for i in open("requirements.txt").readlines()]


setuptools.setup(
    name="transkun",
    version="0.1.0",
    author="Yujia Yan",
    description='Yet another tool for automatic piano transcription',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yujia-Yan/Skipping-The-Frame-Level",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    include_package_data = True,
    python_requires=">=3.6",
    entry_points={
        'console_scripts':[
            'transkun = transkun.transcribe',
            'transkunEval = transkun.computeMetrics'
        ]
    },
    install_requires=[
        requirements
    ],

)