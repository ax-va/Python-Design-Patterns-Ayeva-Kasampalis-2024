"""
Proxy

The Proxy design pattern contains:

- a *virtual proxy*, which uses *lazy initialization* to defer
the creation of a computationally expensive object until the moment it is actually needed;

- a *protection/protective proxy*, which controls access to a sensitive object;

- a *remote proxy*, which acts as the local representation of an object that really exists
in a different address space (for example, a network server); an example: an object-relational mapping (ORM) API;

- a *smart (reference) proxy*, which performs extra actions when an object is accessed;
examples: reference counting and thread-safety checks.
"""


# A `LazyProperty` class is a decorator and acts as a descriptor to implement lazy loading of properties
class LazyProperty:
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        print(f"Function overridden: {self.method}")
        print(f"Function's name: {self.method_name}")

    # descriptor method
    def __get__(self, obj, cls):
        # Handle the case where the descriptor is accessed
        # through the class itself like `Test.resource`,
        # rather than through an instance like `t.resource`.
        if not obj:
            return None
        value = self.method(obj)
        print(f'Value {value}')
        setattr(obj, self.method_name, value)
        return value


# Lazily load the `_resource` attribute only when it is accessed for the first time
# and override the `resource` method with the initialized value.
class Test:
    def __init__(self):
        # two regular attributes
        self.x = "foo"
        self.y = "bar"
        # lazy attribute
        self._resource = None

    @LazyProperty
    def resource(self):
        print("Initializing self._resource...")
        print(f"... which is: {self._resource}")
        self._resource = tuple(range(5))
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    # do more work...
    # 1. The `_resource` variable is initialized by the first time that we use `t.resource`.
    print(t.resource)  # The `LazyProperty`'s `__get__` method is called with `obj=t` and `cls=Test`.
    # 2. The second time `t.resource` is used, the variable is not initialized again.
    print(t.resource)  # Return the previously computed value.


if __name__ == "__main__":
    main()
    # Function overridden: <function Test.resource at 0x7033a04e2020>
    # Function's name: resource
    # foo
    # bar
    # Initializing self._resource...
    # ... which is: None
    # Value (0, 1, 2, 3, 4)
    # (0, 1, 2, 3, 4)
    # (0, 1, 2, 3, 4)