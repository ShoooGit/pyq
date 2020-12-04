def func(arg1: str, arg2: int = 0) -> list:
    print(func.__annotations__)
    return [arg1, arg2]

print(func.__annotations__)