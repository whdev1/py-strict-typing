from copy import copy
from inspect import signature
from typing import get_type_hints, Union
from types import FunctionType as function

class _typed_function:
    __origcall__    = None
    __params__      = None
    __types__       = None

    def __init__(self, func: function):
        self.__origcall__ = func.__call__
        self.__params__ = list(signature(func).parameters.keys())
        self.__types__ = get_type_hints(func)
        
        # check for a return type
        if 'return' in self.__types__.keys():
            self.__returntype__ = self.__types__['return']

    def __call__(self, *args, **kwargs):
        params_copy = copy(self.__params__)

        # type check all kwargs
        for key in kwargs:
            if key in self.__types__.keys():
                if not issubclass(kwargs[key].__class__, self.__types__[key]):
                    raise TypeError(
                        'object of type \'' + str(kwargs[key].__class__.__name__)+ '\' cannot be assigned '
                        'to parameter \'' + key + '\' of type \'' + str(self.__types__[key].__name__) + '\''
                    )
                params_copy.remove(key)
            else:
                params_copy.remove(key)

        # type check all positional args
        for n in range(len(args)):
            if params_copy[n] in self.__types__.keys():
                if not issubclass(args[n].__class__, self.__types__[params_copy[n]]):
                    raise TypeError(
                            'object of type \'' + str(args[n].__class__.__name__)+ '\' cannot be assigned '
                            'to parameter \'' + params_copy[n] + '\' of type \'' + str(self.__types__[params_copy[n]].__name__) + '\''
                    )

        # call the function that we are wrapping
        retval = self.__origcall__(*args, **kwargs)

        # if a return type was specified, check the return type
        if hasattr(self, '__returntype__'):
            if not issubclass(retval.__class__, self.__returntype__):
                raise TypeError(
                            'object of type \'' + str(retval.__class__.__name__)+ '\' cannot be assigned '
                            'to return value of type \'' + str(self.__returntype__.__name__) + '\''
                    )

        return retval

def _checked_setattr(inst: object, name: str, attr: object) -> None:
    # check if this attribute has a type hint
    if name in inst.__types__.keys():
        # if it does, ensure that the object being passed is of the correct type
        if issubclass(attr.__class__, inst.__types__[name]):
            inst.__origsetattr__(name, attr)
        else:
            # if it is not the correct type, throw an error
            raise TypeError(
                'object of type \'' + str(attr.__class__.__name__) + '\' cannot be ' +
                'assigned to member \'' + name + '\' of type \'' + str(inst.__types__[name].__name__) + '\''
            )
    # otherwise, if this attribute has no type hint
    else:
        # check that the attribute has been declared
        if hasattr(inst, name):
            inst.__origsetattr__(name, attr)
        else:
            # if not, throw an error
            raise NameError('object has no attribute \'' + name + '\'')

def strictly_typed(class_def: Union[type, function]):
    """
    A decorator that allows Python classes and functions to enforce strict typing.
    Additionally, disallows assignment to class attributes that have not been declared.
    """

    # check if the received object is a class or a function
    if issubclass(class_def.__class__, type):
        # define the __types__ member which will contain a direct reference to type hints
        class_def.__types__ = get_type_hints(class_def)

        # ensure that all attributes are initialized. if not, initialize them to None
        for key in class_def.__types__:
            if key not in class_def.__dict__.keys():
                setattr(class_def, key, None)

        # swap out the existing __setattr__ function for our checked one. preserve
        # the original as __origsetattr__
        class_def.__origsetattr__ = class_def.__setattr__
        class_def.__setattr__ = _checked_setattr
    elif issubclass(class_def.__class__, function):
        class_def = _typed_function(class_def)
    else:
        raise TypeError(
            'cannot apply strictly_typed decorator to objects of type ' + str(type(class_def).__name__)
        )

    # simply return the class or function defintion
    return class_def