def make_linear(lst):
    lst_linear = []
    for item in lst:
        if type(item) is list:
            lst_linear.extend(make_linear(item))
        else:
            lst_linear.append(item)
    return lst_linear



print(make_linear([1, [3, [6, 5]]]))