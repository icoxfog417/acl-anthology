# Acl-Anthology

**ACL published the official package to access ACL Anthology! Please use [acl-anthology-py](https://github.com/acl-org/acl-anthology) instead of this repository.**

Script to get [ACL Anthology](https://www.aclweb.org/anthology/)

[Pre-downloaded data is available at Kaggle](https://www.kaggle.com/takahirokubo0/acl-anthology-papers/home)


## Install

```
pip install acl-anthology
```

## How to use

```
from acl.conference import Conference


Conference.ACL(2018).retrieve("P18-5").to_dataframe().to_csv("acl2018.csv", index=False)
```
