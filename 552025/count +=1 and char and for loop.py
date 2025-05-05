def gela(s):
    count = 0
    for char in s:
        #gadayavs didi asoebi patara asoebshi "char.lower()"
        if char.lower() in "aeiou":
            count += 1
    return count

print(gela("AaeEiIoOuU"))