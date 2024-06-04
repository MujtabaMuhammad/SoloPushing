NATO_DICT = {'A':'Alfa', 'B':'Bravo', 'C':'Charlie', 'D':'Delta',
'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'H':'Hotel', 'I':'India',
'J':'Juliett', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November',
'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra',
'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray',
'Y':'Yankee', 'Z':'Zulu',}


def nato_language ():
    txt = input("Please enter the text you'd like converted into NATO: ")
    text = txt.upper()
    final_combo = []
    for i in text:
        for k , v in NATO_DICT.items():
            if i == k:
                final_combo.append(v)
    final_text = ' '.join(final_combo)
    print(final_text)


nato_language()