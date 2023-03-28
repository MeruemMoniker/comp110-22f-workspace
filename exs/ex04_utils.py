"""Utils time wew"""
__author__: 123456789

def all(lip: list = [str], a: int = ()) -> bool:
    i: int = 0
    while i < len(lip):
        if a == lip[i]:
            i += 1
        else:
            return False
    return True

def max(lips: list = [int]) -> int:
    if len(str(lips)) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    t: int = 0
    z: int = 0
    while i < len(lips):
        if z > lips[t]:
            t += 1
        else:
            z = int = lips[t]
            t += 1
        i += 1
    return z

def is_equal(lipa: list[int], lipB: list[int]) -> bool:
    i: int = 0
    while i < len(lipa):
        if lipa[i] == lipB[i]:
            i += 1
        else:
            return False
    return True
