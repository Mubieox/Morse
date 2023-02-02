def TTM(Text):
    Text=Text.lower()
    Text=Text.split()
    final=""
    Tradtm={"a":"*-","b":"-***","c":"-*-*","d":"-**","e":"*","f":"**-*","g":"--*","h":"***","i":"**","j":"*---","k":"-*-","l":"*-**","m":"--","n":"-*","o":"---","p":"*--*","q":"--*-","r":"*-*","s":"***","t":"-","u":"**-","v":"***-","w":"*--","x":"-**-","y":"-*--","z":"--**"}
    for mot in range(len(Text)):
        Morse=""
        for lettre in range(len(Text[mot])):
            if Text[mot][lettre] in Tradtm.keys():
                Morse+=Tradtm[Text[mot][lettre]]+" "
            else:
                Morse+=Text[mot][lettre]+"  "
        final+=Morse+"  "
    return final

def MTT(Morse):
    Morse=Morse.split("  ")
    final=""
    Tradmt={"*-":"a","-***":"b","-*-*":"c","-**":"d","*":"e","**-*":"f","--*":"g","***":"s","**":"i","*---":"j","-*-":"k","*-**":"l","--":"m","-*":"n","---":"o","*--*":"p","--*-":"q","*-*":"r","-":"t","**-":"u","***-":"v","*--":"w","-**-":"x","-*--":"y","--**":"z"}
    #temp=dict((value, key) for key, value in Tradmt.items())
    #print(temp)
    #Tradmt=temp 
    for mot in range(len(Morse)):
        Text=""
        Morse[mot]=Morse[mot].split()
        for lettre in Morse[mot]:
            if lettre in Tradmt.keys():
                Text+=Tradmt[lettre]
            else:
                Text+=lettre
        final+=Text+" "
    return final

t="Bonjour la France!"
m=TTM(t)
tt=MTT(m)
print(m)
print(tt)