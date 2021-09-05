"""CP1404 Hex Colours program"""


HEX_COLOUR_CODES = {"aliceblue": "#f0f8ff",
                    "antiquewhite": "faebd7",
                    "aquamarine1": "#7fffd4",
                    "azure1": "#f0fffff",
                    "beige": "#838b8b",
                    "bisque1": "#ffe4c4",
                    "black": "000000",
                    "blue1": "#0000ff",
                    "brown": "a52a2a",
                    "BlueViolet": "#8a2be2"}

hex_colour = input("Enter Hex colour: ").lower()
while hex_colour != "":
    if hex_colour in HEX_COLOUR_CODES:
        print(hex_colour, "is", HEX_COLOUR_CODES[hex_colour])
    else:
        print("Invalid Hex colour")
    hex_colour = input("Enter Hex colour: ").lower()
