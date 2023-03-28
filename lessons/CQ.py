i:int = 0
def contains(needle: int, hs = list[int]) -> bool:
    i = 0
    while i < len(hs):
        if needle == hs[i]:
            print("True")
            return True
        else:
            i += 1
    print("False")
    return False