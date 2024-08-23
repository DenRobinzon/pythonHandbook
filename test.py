from sys import stdin

query = input()
files = stdin.read().split()

query_modified = ''.join(query.split()).lower()
files_with_query = []

for file in files:
    with open(file, encoding='UTF-8') as file_in:
        content = ''.join(file_in.read().split()).lower()
        if query_modified in content:
            files_with_query.append(file)

if files_with_query:
    print(*files_with_query, sep='\n')
else:
    print('404. Not Found')
