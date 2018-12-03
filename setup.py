from setuptools import setup


setup(
    name="acl-anthology",
    version="0.1.0",
    description="Get ACL Anthology Papers.",
    keywords=["machine learning", "nlp", "natural language processing"],
    author="icoxfog417",
    author_email="icoxfog417@yahoo.co.jp",
    license="MIT",
    packages=[
        "acl",
        ],
    url="https://github.com/icoxfog417/acl-anthology",
    install_requires=[
        "requests>=2.20.1",
        "beautifulsoup4>=4.6.3",
        "arxiv>=0.2.2",
        "pandas>=0.23.4",
        "tqdm>=4.28.1"
    ],
)
