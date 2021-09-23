# Python Strong Typing
This is a runtime library that allows Python classes to enforce strong typing of their members at declaration and assignment and Python functions to have type-checked parameters and return values. It supplies a `@strongly_typed` decorator that may be applied to any class or function to enable type checking.

## Installation
This library is available via PyPI. It may be installed with the following pip command:

```
pip install py-strong-typing
```

## Usage

### With Classes
Any class may declare itself as having strongly-typed members using the `@strongly_typed` decorator:

```Python
from strong_typing import *

@strongly_typed
class example_class:
    a: int
    b: int

print(example_class.a)    # None
```

Upon assignment, any member of an instance of the class that provides a type hint will be type checked on assignment:

```Python
example_inst = example_class()

example_inst.a = 123
print(example_inst.a)       # 123
example_inst.a = 'hello'    # results in TypeError
```

Any members that do not have a type hint will not be checked. Also note that static assignments at the time of class declaration cannot be checked.

```Python
from strong_typing import *

@strongly_typed
class example_class:
    a = 'hello'
    b: list = 123   # valid. static assignment at declaration is not checked

inst = example_class()
inst.a = 123        # valid. 'a' has no hint so it is not checked
```

### With Functions
Any Python function may declare its parameters and return type as strongly-typed using the `@strongly_typed` directive:

```Python
from strong_typing import *

@strongly_typed
def test(a: int, b: str) -> str:
    return str(a) + b

print(test(123, 'hello'))           # returns '123hello'
print(test(10.0, 'invalid'))        # results in TypeError
```

As with strongly-typed classes, any parameters that lack a hint will not be checked.

```Python
from strong_typing import *

@strongly_typed
def test(a, b: str) -> str:
    return str(a) + b

print(test(10.0, 'not invalid'))    # returns '10.0not invalid' as 'a' is no longer checked.
```

This rule also applies to the return type hint:

```Python
from strong_typing import *

@strongly_typed
def test(a: int):
    return a + 123

@strongly_typed
def test2(a: int) -> str:
    return a + 123

print(test(111))        # outputs '234'
print(test2(111))       # results in TypeError
```