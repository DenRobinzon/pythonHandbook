import itertools

suits = {'буби': 'бубен',
         'пики': 'пик',
         'трефы': 'треф',
         'черви': 'червей'}

faces = ['10', '2', '3', '4', '5', '6', '7', '8',
         '9', 'валет', 'дама', 'король', 'туз']



suit = input()
face = input()
previous_option = input()

faces.remove(face)

cards = itertools.product(faces, suits.values())
three_cards = [selection for selection in itertools.combinations(cards, 3)
               if suits[suit] in itertools.chain.from_iterable(selection)]
three_cards_2 = [selection for selection in itertools.combinations(cards, 3)
               if suits[suit] in itertools.chain.from_iterable(selection)]

print(three_cards, three_cards_2, sep='\n')
printed = False
#
# while not printed:
#     if (', '.join((f'{f} {s}' for f, s in next(three_cards)))) == previous_option:
#         print(', '.join((f'{f} {s}' for f, s in next(three_cards))))
#         printed = True
