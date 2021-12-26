[![PyPI version](https://badge.fury.io/py/py-code-meli.svg)](https://badge.fury.io/py/py-code-meli)


This project is following this Unix philosophy:  [DOTADIW](https://en.wikipedia.org/wiki/Unix_philosophy#Do_One_Thing_and_Do_It_Well)


____

So the project do a simple task.. validate code meli (Iranian National Code)..thats it..!



the algorithem is explained in Persian in [this site](http://www.aliarash.com/article/codemeli/codemeli.htm)

___
## How to use it?

to install it, run:
>`pip install py-code-meli`

```python
>>>from py_code_meli import is_valid
>>>is_valid("0095017240")
True
>>>is_valid("0095017241")
False
```


___
### Run Tests

to run the package tests, first you need to clone it and then  run :

>`poetry install`

to run the tests:
>`poetry run pytest`


____
**to generate valid code meli, use this [link](http://mellicode.azmads.com/Home/Index?id=0)**