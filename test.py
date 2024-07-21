title = ''
length = int(input())
lines = int(input())
short_title = None

for i in range(lines):
    title += input()
    if (not short_title) and len(title) - i >= length - 3:
        short_title = title[:length + i - 3] + '...'
    title += '\n'

if not short_title:
    short_title = title

print(short_title)






