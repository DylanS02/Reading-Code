# Purpose:

def ask(type_of_word):
    word = input("Please enter a " + type_of_word + ": ")
    return word

def get_responses(words_needed):
    from_user = {}
    for word_type in words_needed:
        from_user[word_type] = ask(word_type)
    return from_user
    
def types_needed(output):
    type_list = []
    parts = output.split("*")
    for i in range(1, len(parts), 2):
        type_list.append(parts[i])
    return type_list

def replace_parts(output, replacements):
    parts = output.split("*")
    for section in parts:
        if section not in replacements:
            print(section, end="")
        else:
            print(replacements[section], end="")
         

thing = """
“Hello. My name is Inigo Montoya. You *verb with -ed* my *relative*. Prepare to *verb*.” – The Princess Bride

“I’ll get you, my *adjective* and your little *noun* too!” – The Wizard of Oz
"""

types = types_needed(thing)
responses = get_responses(types)
replace_parts(thing, responses)
    

