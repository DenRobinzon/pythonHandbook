# A.Обработка ошибок
try:
    func()
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')
except SystemError:
    print('SystemError')
else:
    print('No Exceptions')

# B.Ломать — не строить
func((), '2')
# C.Полное решение
# Ломать — не строить 2
class Bad:
    def __repr__(self):
        return


print(func(Bad()))

# D.
# E.
# F.
# G.
# H.
# I.
# J.
# K.
# L.
# M.
# N.
# O.
# P.
# Q.
# R.
# S.
# T.