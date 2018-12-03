# Acl-Anthology

Script to get [ACL Anthology](https://aclanthology.info/)


## Install

```
pip install acl-anthology
```

## How to use

```
from acl.conference import Conference


Conference.ACL(2018).retrieve("P18-5").to_dataframe().to_csv("acl2018.csv", index=False)
```
