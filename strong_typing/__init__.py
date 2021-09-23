from typing import get_type_hints

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

def strongly_typed(class_def: type) -> type:
    """
    A decorator that allows Python classes to enforce strong typing of their members
    and disallows assignment to attributes that have not been declared
    """

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

    # simply return the class defintion
    return class_def

globals()['a'] = 123