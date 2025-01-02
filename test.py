def func(a):
    return str(a)


class Bad:
    def __str__(self):
        return


print(func(Bad()))  # noqa F821