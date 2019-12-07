import re


def testpassword(password: int, required_repeat: int = None) -> bool:
    match = True
    comparitor = 0
    repeats = 1
    repeatset = set()
    for i in str(password):
        if int(i) == comparitor:
            repeats += 1
        else:
            if repeats > 1:
                repeatset.add(repeats)
            repeats = 1
        if int(i) < comparitor:
            match = False
        else:
            pass
        comparitor = int(i)
    if repeats > 1:
        repeatset.add(repeats)
    if len(repeatset) == 0:
        match = False
    if required_repeat is not None:
        if required_repeat in repeatset:
            pass
        else:
            match = False
    return match
