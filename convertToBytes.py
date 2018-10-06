
def byteArrayOut():
    with open("happylee-supermariobros,warped.fm2") as f:
        f_array = f.readlines()

        results = []

        for line in f_array:
            if line[0] == '|':
                results.append(strToByte(line[3:11]))

        return bytes(results)


def strToByte(stringRow):
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


def byteToStr(byte):
    buttons = 'RLDUTSBA'
    binString = '{0:08b}'.format(byte)
    buttonString = ''

    for i, digit in enumerate(binString):
        if digit == '1':
            buttonString += buttons[i]
        else:
            buttonString += '.'

    return buttonString

# print(byteArrayOut())
  
# print(byteToStr(0x82))

def generateFM2(byteArray):
    file = open('output.fm2', 'w')

    metadata = {
        "version": input('Version (required): '),
        "emuVersion": input('Emulator version (required): '),
        "rerecordCount": input('Re-record count: '),
        "palFlag": input('Pal flag: '),
        "romFilename": input('ROM file name (required): '),
        "romChecksum": input('ROM Checksum (required): '),
        "guid": input('GUID (required): '),
        "fourscore": input('Fourscore: '),
        "microphone": input('Microphone: '),
        "port0": input('Port 0: '),
        "port1": input('Port 1: '),
        "port2": input('Port 2 (required): '),
        "FDS": input('FDS: '),
        "NewPPU": input('New PPU: '),
        "comment author": input('Comment: ')
    }

    for field, value in metadata.items():
        if bool(value):
            file.write(field + ' ' + value + '\n')
    
    for i, byte in enumerate(byteArray):
        prefix = '|1|' if i == 0 else '|0|'

        file.write(prefix + byteToStr(byte) + '|........||' + '\n')


generateFM2(byteArrayOut())