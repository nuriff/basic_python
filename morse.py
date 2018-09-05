MORSE_CODE_DICT = { 'A':'.-', 
'B':'-...', 
'C':'-.-.', 
'D':'-..', 
'E':'.', 
'F':'..-.', 
'G':'--.', 
'H':'....', 
'CH':'----', 
'I':'..', 
'J':'.---', 
'K':'-.-', 
'L':'.-..', 
'M':'--', 
'N':'-.', 
'O':'---', 
'P':'.--.', 
'Q':'--.-', 
'R':'.-.', 
'S':'...', 
'T':'-', 
'U':'..-', 
'V':'...-', 
'W':'.--', 
'X':'-..-', 
'Y':'-.--', 
'Z':'--..'}

zprava = input().upper()

def encrypt(zprava):
    text = ''
    for pismeno in zprava:
        if pismeno != ' ':
            text += MORSE_CODE_DICT[pismeno] + ' '
        else:
            text += ' '
    return text
def decrypt(zprava):
    text = ' '
    zprava += ' '
    desifrovat = ''
    citext = ''
    for pismeno in zprava:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
  return decipher

def main():
    result = encrypt(zprava.upper())
    print (result)

    result = decipher(zprava)
    print (result)
    
if __name__ == '__main__':
    main()
