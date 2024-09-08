def make_linear(lst):
    for i in range(len(lst)):
        if type(lst[i]) is list:
            lst = lst[:i] + make_linear(lst[i]) + lst[i + 1:]
    else:
        return lst


print(make_linear([1, [3, [6, 5]]]))
