from typing import List

def get_fuel(mass: int, recursive: bool = False) -> int :
    initial = (mass//3) -2
    if initial > 0:
        yield initial
        if recursive:
            yield from get_fuel(initial, recursive)
    else:
        pass

def get_fuel_list(masses: List[int], recursive: bool = False) -> List[int]:
    full_list = []
    for i in masses:
        full_list.extend(list(get_fuel(i, recursive)))
    return full_list

def get_fuel_total(masses: List[int], recursive: bool = False) -> int:
    return sum(get_fuel_list(masses, recursive))
