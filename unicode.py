#Superscripts
numunicode = ["\u2070","\u00b9","\u00b2","\u00b3","\u2074","\u2075","\u2076","\u2077","\u2078","\u2079"]
alphaunicode = ["\u1D43","\u1D47","\u1D9C","\u1D48","\u1D49","\u1DA0","\u1D4D","\u02B0","\u2071","\u02B2","\u1D4F","\u02E1","\u1D50","\u207F","\u1D52","\u1D56","\u02B3","\u02E2","\u1D57","\u1D58","\u1D5B","\u02B7","\u02E3","\u02B8"]
alphalist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y']

#Subscripts
numunicode2 = ["\u2080","\u2081","\u2082","\u2083","\u2084","\u2085","\u2086","\u2087","\u2088","\u2089"]

#Math Symbols
raw = ["chia","=","!=","<=",">=","vocuc","tongsigma","tich","tichphan","delta","canbac2","do","phantram","phannghin"]
unicodekyhieu = ["\u00F7","\u003D","\u2260","\u2264","\u2265","\u221E","\u2211","\u220F","\u222B","\u2202","\u221A","\u221B","\u221C","\u00B0","\u0025","\u0030"]

def mutren(kytu):
    # Số nguyên
    def superint(num):
        if 0 <= num < 10:
            for x in range(10):
                if num == x:
                    result = numunicode[x]
        elif num >= 10:
            uni = []
            digits = [int(digit) for digit in str(num)]
            for n in digits:
                for x in range(10):
                    if n == x:
                        s = numunicode[x]
                        uni.append(s)
            result = str("".join(uni))
        elif num < 0:
            num = -num
            for x in range(10):
                if num == x:
                    result = f'-{numunicode[x]}'
        return result
    #Số thực
    def superfloat(num):
        unithuc = []
        unithapphan = []
        soAm = False
        if num < 0:
            num = -num
            soAm = True
        nguyen = int(num)
        thapphan = num - nguyen
        thapphan = str(thapphan)
        thapphan = thapphan.replace(".","")
        thapphan = int(thapphan)
        thapphan = [int(x) for x in str(thapphan)]
        thuc = [int(x) for x in str(nguyen)]
        for n in thuc:
            for x in range(10):
                if n == x:
                    s1 = numunicode[x]
                    unithuc.append(s1)
        ketquathuc = str("".join(unithuc))
        for n in range(len(thapphan)):
            for x in range(10):
                if thapphan[n] == x:
                    s2 = numunicode[x]
                    unithapphan.append(s2)
        ketquathapphan = str("".join(unithapphan))
        ketqua = f"{ketquathuc}`{ketquathapphan}"
        if soAm == True:
            ketqua = f'-{ketqua}'
        return ketqua
    #Ký tự thường từ a-z
    def superalpha(alpha):
        chars = []
        if alpha == 'q' or alpha == 'z':
            return None
        else:
            for x in range(len(alphalist)):
                if alpha == x:
                    s = alphaunicode[x]
                    chars.append(s)
        ketqua = str("".join(chars))
        return ketqua
    if isinstance(kytu, int):
        return superint(kytu)
    if isinstance(kytu, float):
        return superfloat(kytu)
    if kytu.isdigit():
        kytu = int(kytu)
        return superint(kytu)
    else:
        try:
            float(kytu)
            if int(kytu) == float(kytu):
                return superint(kytu)
            else:
                return superfloat(kytu)
        except ValueError:
            return superalpha(kytu)
def kyhieutoanhoc(kyhieu):
    for x in range(len(raw)):
        if raw[x] == kyhieu:
            return unicodekyhieu[x]
def muduoi(kytu):
    def subint(num):
        if 0 <= num < 10:
            for x in range(10):
                if num == x:
                    result = numunicode2[x]
        elif num >= 10:
            uni = []
            digits = [int(digit) for digit in str(num)]
            for n in digits:
                for x in range(10):
                    if n == x:
                        s = numunicode2[x]
                        uni.append(s)
            result = str("".join(uni))
        elif num < 0:
            num = -num
            for x in range(10):
                if num == x:
                    result = f'-{numunicode2[x]}'
        return result
    

    if isinstance(kytu, int):
        return subint(kytu)
    '''
    if isinstance(kytu, float):
        return subfloat(kytu)
    if kytu.isdigit():
        kytu = int(kytu)
        return superint(kytu)
    else:
        try:
            float(kytu)
            if int(kytu) == float(kytu):
                return superint(kytu)
            else:
                return superfloat(kytu)
        except ValueError:
            return superalpha(kytu)
    '''