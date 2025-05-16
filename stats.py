def get_book_text(book_file): 
    with open(book_file) as text:
        file_contents = text.read()
        return file_contents

def count_words(book_file):
    words = get_book_text(book_file).split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def character_count(book_file):
    def dict_key(entry):
        return entry["num"]
    
    character_dictionary = {}
    for word in get_book_text(book_file).split():
        for character in word.lower():
            if character.isalpha():
                if character not in character_dictionary:
                    character_dictionary[character] = 1
                else:
                    current_value = 0
                    current_value = character_dictionary.get(character)
                    character_dictionary.update({character: current_value + 1})   
            else:
                pass    
    
    sorted_dictionary = []
    for char, num in character_dictionary.items():
        sorted_dictionary.append({"char": char , "num": num})
    sorted_dictionary.sort(reverse=True,key=dict_key)
    return sorted_dictionary
