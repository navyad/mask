[![build status](https://github.com/navyad/mask/actions/workflows/main.yml/badge.svg)](https://github.com/navyad/mask/actions/workflows/main.yml/badge.svg) [![codecov](https://codecov.io/gh/navyad/mask/branch/master/graph/badge.svg?token=WVEW7WBD1A)](https://codecov.io/gh/navyad/mask)

<div align="center">
<h1 style="color:red;font-size:100px;">mask (WIP)</h1> 
<img src="https://user-images.githubusercontent.com/1172317/232051551-aa101f2b-dfa0-4254-a125-dc159e56aad6.png">
</div>


# Why mask ?
I am sure, you do not want expose sensitive information.


## Mask Types

|Type         |Description                                         |
|:-----------:|:---------------------------------------------------|
|EMAIL        |keep first three chars and domain.                  |
|PASSWORD     |all characters are masked.                          |



## Usage

```python
>>> from mask import mask, MaskType

>>> mask(MaskType.EMAIL, "reliko9368@lieboe.com")
rel*******@lieboe.com

>>> mask(MaskType.PASSWORD, "123@KBC$fdcDED")
**************
```

