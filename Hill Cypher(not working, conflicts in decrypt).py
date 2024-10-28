def cypher(x, y):
    if y == "encrypt":
        replacements = {
            "a": "485",
            "b": "915",
            "c": "584",
            "d": "596",
            "e": "475",
            "f": "433",
            "g": "037",
            "h": "058",
            "i": "643",
            "j": "916",
            "k": "978",
            "l": "513",
            "m": "224",
            "n": "375",
            "o": "839",
            "p": "834",
            "q": "097",
            "r": "524",
            "s": "654",
            "t": "036",
            "u": "650",
            "v": "415",
            "w": "599",
            "x": "905",
            "z": "798"
        }

        for char, num in replacements.items():
            x = x.replace(char, f"#{num}#")  # Use # to avoid conflicts

        # Remove temporary markers
        for num in replacements.values():
            x = x.replace(f"#{num}#", num)

        return x

    elif y == "decrypt":
        replacements = {
            "485": "a",
            "915": "b",
            "584": "c",
            "596": "d",
            "475": "e",
            "433": "f",
            "037": "g",
            "058": "h",
            "643": "i",
            "916": "j",
            "978": "k",
            "513": "l",
            "224": "m",
            "375": "n",
            "839": "o",
            "834": "p",
            "097": "q",
            "524": "r",
            "654": "s",
            "036": "t",
            "650": "u",
            "415": "v",
            "599": "w",
            "905": "x",
            "798": "z"
        }

        for num, char in replacements.items():
            x = x.replace(num, char)
        return x


# Example usage
x = input("text: ")
y = input("encrypt/decrypt?: ")
y = y.lower()
result = cypher(x, y)
print(result)
