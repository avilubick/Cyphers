import re
def cypher(x,y,z):
    if z == "ceaser":
        encrypt = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "zabcdefghijklmnopqrstuvwxyZABCDEFGHIJKLMNOPQRSTUVWXY")
        decrypt = str.maketrans("zabcdefghijklmnopqrstuvwxyZABCDEFGHIJKLMNOPQRSTUVWXY", "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if y == "encrypt":
            return x.translate(encrypt)
        elif y == "decrypt":
            return x.translate(decrypt)
        else:
            print("Error")
    elif z == "substitution":
        if y == "encrypt":
            replacements = str.maketrans("abcdefghijklmnopqrstuvwxyz", "%-[}&!*^$/=#_=+>.{@:<])?(;")
            return x.translate(replacements)
        elif y == "decrypt":
            replacements = str.maketrans("%-[}&!*^$/=#_=+>.{@:<])?(;", "abcdefghijklmnopqrstuvwxyz")
            return x.translate(replacements)

def prompt():
    d = input("cypher/detection: ")
    if d == "detection":
        g=input("cypher: ")
        if g.isdigit() == True:
            g = bool(g)
            g == g / 3
            if g.isdigit() == True:
                print("hill cypher")
                prompt()
            else:
                print("not recognised")
                prompt()
        else:
            if re.search('[a-zA-Z]', g) == None and g.isnumeric() == False:
                print("substitution cypher")
                prompt()
            else:
                print("not recognised")
                prompt()

    else:
        x=input("text: ")
    if x == "exit":
        exit()
    else:
        pass
    z = input("cypher type?(ceaser/substitution): ")
    if z == "ceaser":
        pass
    elif z == "substitution":
        x = x.lower()
    else:
        print("invalid")
        prompt()
    y = input("encrypt/decrypt?: ")
    z = z.lower()
    y = y.lower()
    if y == "encrypt":
        pass
    elif y == "decrypt":
        pass
    else:
        prompt()
        print("invalid")
    x = cypher(x,y,z)
    print(x)
    prompt()

prompt()

