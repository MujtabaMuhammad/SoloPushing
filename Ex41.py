NATO_DICT = {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
             'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India',
             'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November',
             'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra',
             'T': 'Tango', 'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
             'Y': 'Yankee', 'Z': 'Zulu'}
def nato_translator():
    user_choice = input("Do you want to convert to or from nato ? ")
    txt_for_conversion = input("Enter the text for conversion: ")
    txt = txt_for_conversion.upper()
    txt_tobe_converted_from_nato = txt.split()
    txt_converted_to_nato = []
    final_list_converted_to_nato = []
    if user_choice.lower() == "from":
        for i in txt:
            for k,v in NATO_DICT.items():
                if i == k :
                    txt_converted_to_nato.append(v)
        final_txt_converted_to_nato = ' '.join(txt_converted_to_nato)
        print(txt_tobe_converted_from_nato)
        quit()
    elif user_choice.lower() == "to":
        for i in txt:
            for k,v in NATO_DICT.items():
                if i == k:
                    final_list_converted_to_nato.append(v)
        ''.join(final_list_converted_to_nato)
        print(final_list_converted_to_nato)

nato_translator()


