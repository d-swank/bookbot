def number_of_words(text):
    return len(text.split())

def number_of_characters(text):
    characters_dict = {}
    for char in text:
        char = char.lower()
        if char not in characters_dict:
            characters_dict[char] = 1
        else:
            characters_dict[char] += 1
    return characters_dict

def sorted_on(items):
    return items['num']

def sorted_dictionaries(char_dict):
    sorted_list = []
    for char in char_dict:
        new_dict = {"char": char, "num": char_dict[char]}
        sorted_list.append(new_dict)
    sorted_list.sort(key=sorted_on, reverse=True)
    return sorted_list

    