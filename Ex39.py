MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',' ':'/',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def morse_coder():
    global MORSE_CODE_DICT
    to_or_from = input("Do you want to convert to or from morse code? ")
    if to_or_from.lower() == "to":
        txt = input("Please enter text in english : ")
        text = list(txt.upper())
        morse_code_text = []
        for i in text:
            morse_code_text.append(MORSE_CODE_DICT.get(i))
        final = ' '.join(morse_code_text)
        print(final)
        quit()
    elif to_or_from.lower() == "from":
        txt = input("Input Morse code: ")
        mc_list = txt.strip().split()
        translated_list = []
        for morse_code in mc_list:
            for k, v in MORSE_CODE_DICT.items():
                if morse_code == v:
                    translated_list.append(k)
        final_phrase = ''.join(translated_list)
        print(final_phrase)
        quit()
    else:
        print("invalid input, quitting program")
        quit()

morse_coder()