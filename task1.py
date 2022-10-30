ans = {key: line.count(key) for key in line if key.isalpha()}
print(ans)
def letters_count(line: str):
    line = line.lower()
    return {key: line.count(key) for key in line if key.isalpha()}

def letters_percent(symbols: dict):
    summa = sum(x for x in symbols.values())
    return {key: symbols[key] / summa for key in symbols}