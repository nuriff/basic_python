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

def main():
    result = encrypt(zprava.upper())
    print (result)

if __name__ == '__main__':
    main()
