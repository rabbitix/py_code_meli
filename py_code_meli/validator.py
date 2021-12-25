

def validate_meli_code(value: str) -> bool:
    if not len(value) == 10:
        # raise ValueError("کد ملی باید ۱۰ رقم باشد.")
        return False

    res = 0
    for i, num in enumerate(value[:-1]):
        res = res + (int(num) * (10 - i))

    remain = res % 11
    if remain < 2:
        if not remain == int(value[-1]):
            # raise ValueError("کد ملی درست نیست")
            return False
    else:
        if not (11 - remain) == int(value[-1]):
            # raise ValueError("کد ملی درست نیست")
            return False

    return True
