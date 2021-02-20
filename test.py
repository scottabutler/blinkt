def hex_to_rgb(hex):
    if (len(hex) == 3):
        return str(int(hex[0:1], 16)) + "," + str(int(hex[1:2], 16)) + "," + str(int(hex[2:3], 16))
    elif (len(hex) == 6):
        return str(int(hex[0:2], 16)) + "," + str(int(hex[2:4], 16)) + "," + str(int(hex[4:6], 16))

print(hex_to_rgb("abc"))

print(hex_to_rgb("aabbcc"))

print(hex_to_rgb("111"))

print(hex_to_rgb("121212"))