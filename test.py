def is_palindrome(object):
    if type(object) is int:
        object = str(object)
    return object == object[::-1]