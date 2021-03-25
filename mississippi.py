word_dict = {"M":0,"I":0,"S":0,"P":0}
word = "MISSISSIPPI"
for i in word:
    if i == "M":
        word_dict['M'] = word_dict['M']+1
    elif i == "I":
        word_dict['I'] = word_dict['I']+1
    elif i == "S":
        word_dict['S'] = word_dict['S']+1
    elif i == "P":
        word_dict['P'] = word_dict['P']+1
print(word_dict)