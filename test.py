import itertools


def secret_replace(text, **replaces):
    replaces_cycled = {k: itertools.cycle(v) for k, v in replaces.items()}
    text_decrypted = ''
    for ch in text:
        if ch in replaces_cycled:
            text_decrypted += next(replaces_cycled[ch])
        else:
            text_decrypted += ch
    return text_decrypted


result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)

print(result)
