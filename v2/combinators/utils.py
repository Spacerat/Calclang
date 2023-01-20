def countAtPos(text: str, start: int, toCount: str):
    pos = start
    while pos < len(text) and text[pos] == toCount:
        pos += 1
    return pos - start
