

def stemmer(text):
    txt = text.split(" ")
    for idx, word in enumerate(txt):
        if word[-2:] == "ed" or word[-2:] == "ly":
            txt[idx] = word[:-2]
        elif word[-3:] == "ing":
            txt[idx] = word[:-3]
        if len(txt[idx]) > 8:
            txt[idx] = txt[idx][:8]
    res = ""
    for w in txt:
        res += w + " "
    return res[:-1]

text = "a boy is jumping quickly "
print(stemmer(text))