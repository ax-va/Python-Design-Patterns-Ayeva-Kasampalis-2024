"""
Use `isinstance` instead of `type`.

"""
from collections import UserList


class CustomListA(UserList):
    pass


class CustomListB(UserList):
    pass


# bad practice
def compare_v1(obj):
    if type(obj) in (CustomListA, CustomListB):
        print("It's a custom list!")
    else:
        print("It's a something else!")


# simpler and more flexible
def compare_v2(obj):
    if isinstance(obj, UserList):
        print("It's a custom list!")
    else:
        print("It's a something else!")


if __name__ == "__main__":
    obj1 = CustomListA([1, 2, 3])
    obj2 = CustomListB(["a", "b", "c"])

    compare_v1(obj1)
    # It's a custom list!
    compare_v1(obj2)
    # It's a custom list!
    compare_v2(obj1)
    # It's a custom list!
    compare_v2(obj2)
    # It's a custom list!
