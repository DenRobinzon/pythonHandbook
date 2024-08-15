import itertools

sportsmen = sorted([input() for _ in range(int(input()))])

print(*[', '.join(names) for names in itertools.permutations(sportsmen)], sep='\n')