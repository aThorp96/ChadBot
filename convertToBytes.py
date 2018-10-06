print("start")


def byteArrayOut():
    with open("C:\\Users\\Jacob Justice\\Documents\\hacknc 2018\\happylee-supermariobros,warped.fm2") as f:
        f_array = f.readlines()

        results = []

        for line in f_array:
            if line[0] == '|':
                results.append(stringToByte(line[3:11]))

        return bytes(results)


def stringToByte(stringRow):
    count = 0
    if stringRow[0] != '.': count += 128
    if stringRow[1] != '.': count += 64
    if stringRow[2] != '.': count += 32
    if stringRow[3] != '.': count += 16
    if stringRow[4] != '.': count += 8
    if stringRow[5] != '.': count += 4
    if stringRow[6] != '.': count += 2
    if stringRow[7] != '.': count += 1
    return count

print(byteArrayOut())
