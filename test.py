friends_1 = {}

while names := input().split():
    name1, name2 = names
    friends_1.setdefault(name1, set()).add(name2)
    friends_1.setdefault(name2, set()).add(name1)

friends_2 = {}

for friend_1 in friends_1:
    friends_2[friend_1] = set()
    for friend_2 in friends_1[friend_1]:
        if friend_2 != friend_1:
            friends_2[friend_1].update(friends_1[friend_2] - {friend_1} - friends_1[friend_1])


for name in sorted(friends_2):
    print(f'{name}: {', '.join(sorted(friends_2[name]))}')
