import string
def is_cyrillic(text: str) -> bool:
    lower_text = text.lower()
    no_space = lower_text.replace(' ', '')
    no_punct = str.maketrans('', '', string.punctuation)
    cleaned = no_space.translate(no_punct)
    cyrillic = False
    for char in cleaned:
        if 'А' <= char <= 'я' or char == 'ё' or char == 'Ё':
            cyrillic = True

    return cyrillic

def convert_to_cyrillic(text: str) -> str:
    key = {
        'a': 'а',
        'b': 'б',
        'v': 'в',
        'g': 'г',
        'd': 'д',
        'ye': 'е',
        'yo': 'ё',
        'zh': 'ж',
        'z': 'з',
        'i': 'и',
        'yi': 'й',
        'k': 'к',
        'l': 'л',
        'm': 'м',
        'n': 'н',
        'o': 'о',
        'p': 'п',
        'r': 'р',
        's': 'с',
        't': 'т',
        'u': 'у',
        'f': 'ф',
        'x': 'х',
        'ts': 'ц',
        'ch': 'ч',
        'sh': 'ш',
        'shh': 'щ',
        'jj': 'ы',
        'e': 'э',
        'yu': 'ю',
        'ya': 'я',
        'j': 'ь'
    }

    cyrillic_text = ""
    i = 0
    while i < len(text):
        if i + 1 <= len(text):
            if i + 2 <= len(text):
                if i + 3 <= len(text):
                    if text[i:i + 3] == 'shh':
                        cyrillic_text += key['shh']
                        i += 3
                        continue
                two_char = text[i:i + 2]
                if two_char in key:
                    cyrillic_text += key[two_char]

                    i += 2
                    continue
        if text[i] in key:
            cyrillic_text += key[text[i]]
        else:
            cyrillic_text += text[i]
        i += 1
    return cyrillic_text