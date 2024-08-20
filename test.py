with open(input(), 'r', encoding='UTF-8') as file_in:
    lines = file_in.readlines()

new_lines = []

for line in lines:
    new_line = ' '.join(line.replace('\t', '').split())
    if new_line:
        new_lines.append(new_line)

with open(input(), 'w', encoding='UTF-8') as file_out:
    print(*new_lines, sep='\n', file=file_out)
