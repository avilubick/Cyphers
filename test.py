import re
def prompt():
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

prompt()