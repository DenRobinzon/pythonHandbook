text = ''
letters = ''
best_letter = ''
best_result = 0
while (input_string := input()) != 'ФИНИШ':
    text += input_string.replace(' ', '').lower()

for letter in text:
    if letter not in letters:
        letters += letter
        if (result := text.count(letter)) > best_result:
            best_letter = letter
            best_result = result
        elif result == best_result and letter < best_letter:
            best_letter = letter

print(best_letter)






