# Python Strict Typing Library
This is a library written in pure Python that enables runtime type-checking for classes and functions via the use of a single `@strictly_typed` decorator. Classes may enforce strict typing of their members and functions are able to have type-checked parameters and return values via type hints.

## Installation
This library is available via PyPI. It may be installed with the following pip command:

```
pip install py-strict-typing
```

## Usage

### With Classes
Any class may declare itself as having strictly-typed members using the `@strictly_typed` decorator:

```Python
from strict_typing import *

@strictly_typed
class example_class:
    a: int
    b: int

print(example_class.a)    # None
```

Upon assignment, any member of an instance of the class that provides a type hint will be type checked:

```Python
example_inst = example_class()

example_inst.a = 123
print(example_inst.a)       # 123
example_inst.a = 'hello'    # results in TypeError
```

Any members that do not have a type hint will not be checked. Also note that static assignments at the time of class declaration cannot be checked.

```Python
from strict_typing import *

@strictly_typed
class example_class:
    a = 'hello'
    b: list = 123   # valid. static assignment at declaration is not checked

inst = example_class()
inst.a = 123        # valid. 'a' has no hint so it is not checked
```

### With Functions
Any Python function may declare its parameters and return type as strictly-typed using the `@strictly_typed` decorator:

```Python
from strict_typing import *

@strictly_typed
def test(a: int, b: str) -> str:
    return str(a) + b

print(test(123, 'hello'))           # returns '123hello'
print(test(10.0, 'invalid'))        # results in TypeError
```

As with strictly-typed classes, any parameters that lack a hint will not be checked.

```Python
from strict_typing import *

@strictly_typed
def test(a, b: str) -> str:
    return str(a) + b

print(test(10.0, 'not invalid'))    # returns '10.0not invalid' as 'a' is no longer checked.
```

This rule also applies to the return type hint:

```Python
from strict_typing import *

@strictly_typed
def test(a: int):
    return a + 123

@strictly_typed
def test2(a: int) -> str:
    return a + 123

print(test(111))        # outputs '234'
print(test2(111))       # results in TypeError
```