def transform(text):
    for ch in text:
        if ch >= 'a' and ch <= 'z':
            i = ord(ch) + 2
            if i > ord('z'):
                i -= 26
            print(chr(i), end="")
        else:
            print(ch, end="")
    print()
            
if __name__ == "__main__":
    s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    
    transform(s)

    trans = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
    print(s.translate(trans))
    
    transform('map')