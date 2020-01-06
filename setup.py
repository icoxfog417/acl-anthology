from setuptools import setup


setup(
    name="acl-anthology",
    version="0.1.5",
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
        "requests>=2.22.0",
        "beautifulsoup4>=4.8.2",
        "arxiv>=0.5.1",
        "pandas>=0.25.3",
        "tqdm>=4.41.1"
    ],
)
