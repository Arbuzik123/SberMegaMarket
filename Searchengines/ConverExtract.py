from transliterate import translit
def convert_symbols_in_brackets(input_string):
    try:
        start_idx = input_string.find('(')
        end_idx = input_string.find(')')
        if start_idx != -1 and end_idx != -1 and end_idx - start_idx <= 5:
            content = input_string[start_idx + 1:end_idx]
            # Транслитерируем содержимое
            content_transliterated = translit(content, 'ru', reversed=True)
            updated_string = input_string[:start_idx + 1] + content_transliterated + input_string[end_idx:]
            return updated_string
        else:
            return input_string
    except:
        print("NoneBrackets")
        return input_string