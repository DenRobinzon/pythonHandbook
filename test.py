from hashlib import sha256

class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8,
                        possible_chars='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_',
                        at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    if not all(ch in possible_chars for ch in password):
        raise PossibleCharError
    if not any(at_least_one(ch) for ch in password):
        raise NeedCharError
    return sha256(password.encode(encoding='UTF-8')).hexdigest()


print(password_validation((123,)))
