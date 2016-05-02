# -*- coding: utf-8 -*-
def Set(li):
    return dict(zip(range(len(li)),li))

#            ㄱ      ㄲ      ㄴ      ㄷ      ㄸ      ㄹ      ㅁ      ㅂ      ㅃ      ㅅ      ㅆ      ㅇ      ㅈ      ㅉ      ㅊ      ㅋ      ㅌ      ㅍ      ㅎ
choTbl = [ 0x3131, 0x3132, 0x3134, 0x3137, 0x3138, 0x3139, 0x3141, 0x3142,
       0x3143, 0x3145, 0x3146, 0x3147, 0x3148, 0x3149, 0x314a, 0x314b, 0x314c,
       0x314d, 0x314e ]
#             ㅏ      ㅐ      ㅑ      ㅒ      ㅓ      ㅔ      ㅕ      ㅖ      ㅗ      ㅘ      ㅙ      ㅚ      ㅛ      ㅜ      ㅝ      ㅞ      ㅟ      ㅠ      ㅡ      ㅢ      ㅣ
jungTbl = [ 0x314f, 0x3150, 0x3151, 0x3152, 0x3153, 0x3154, 0x3155, 0x3156,
        0x3157, 0x3158, 0x3159, 0x315a, 0x315b, 0x315c, 0x315d, 0x315e, 0x315f,
        0x3160, 0x3161, 0x3162, 0x3163 ]
#                      ㄱ      ㄲ      ㄳ      ㄴ      ㄵ      ㄶ      ㄷ      ㄹ      ㄺ      ㄻ      ㄼ      ㄽ      ㄾ      ㄿ      ㅀ      ㅁ      ㅂ      ㅄ      ㅅ      ㅆ      ㅇ      ㅈ      ㅊ      ㅋ      ㅌ      ㅍ      ㅎ
jongTbl = [ 0,      0x3131, 0x3132, 0x3133, 0x3134, 0x3135, 0x3136, 0x3137,
        0x3139, 0x313a, 0x313b, 0x313c, 0x313d, 0x313e, 0x313f, 0x3140, 0x3141,
        0x3142, 0x3144, 0x3145, 0x3146, 0x3147, 0x3148, 0x314a, 0x314b, 0x314c,
        0x314d, 0x314e ]

UniCodeHangulBase = 0xAC00
UniCodeHangulLast = 0xD79F

choSet = [ 0x3131, 0x3132, 0x3134, 0x3137, 0x3138, 0x3139, 0x3141, 0x3142,
        0x3143, 0x3145, 0x3146, 0x3147, 0x3148, 0x3149, 0x314a, 0x314b, 0x314c,
        0x314d, 0x314e ]
#              ㅏ      ㅐ      ㅑ      ㅒ      ㅓ      ㅔ      ㅕ      ㅖ      ㅗ      ㅘ      ㅙ      ㅚ      ㅛ      ㅜ      ㅝ      ㅞ      ㅟ      ㅠ      ㅡ      ㅢ      ㅣ
jungSet = [ 0x314f, 0x3150, 0x3151, 0x3152, 0x3153, 0x3154, 0x3155, 0x3156,
        0x3157, 0x3158, 0x3159, 0x315a, 0x315b, 0x315c, 0x315d, 0x315e, 0x315f,
        0x3160, 0x3161, 0x3162, 0x3163 ]
#                      ㄱ      ㄲ      ㄳ      ㄴ      ㄵ      ㄶ      ㄷ      ㄹ      ㄺ      ㄻ      ㄼ      ㄽ      ㄾ      ㄿ      ㅀ      ㅁ      ㅂ      ㅄ      ㅅ      ㅆ      ㅇ      ㅈ      ㅊ      ㅋ      ㅌ      ㅍ      ㅎ
jongSet = [ 0,      0x3131, 0x3132, 0x3133, 0x3134, 0x3135, 0x3136, 0x3137,
        0x3139, 0x313a, 0x313b, 0x313c, 0x313d, 0x313e, 0x313f, 0x3140, 0x3141,
        0x3142, 0x3144, 0x3145, 0x3146, 0x3147, 0x3148, 0x314a, 0x314b, 0x314c,
        0x314d, 0x314e ]

#                ㄸ        ㅃ      ㅉ  
ChoOnly = [ 0x3138,  0x3143, 0x3149 ]
#                   ㄳ      ㄵ      ㄶ       ㄺ      ㄻ      ㄼ      ㄽ      ㄾ      ㄿ      ㅀ        ㅄ    
JongOnly = [ 0x3133, 0x3135, 0x3136, 0x313a, 0x313b, 0x313c, 0x313d, 0x313e,
         0x313f, 0x3140, 0x3144 ]
#                  ㅏ      ㅐ      ㅑ      ㅒ      ㅓ      ㅔ      ㅕ      ㅖ      ㅗ      ㅘ      ㅙ      ㅚ      ㅛ      ㅜ      ㅝ      ㅞ      ㅟ      ㅠ      ㅡ      ㅢ      ㅣ


class info(object):
    def __init__(self):
        self.cho = 0
        self.jung = 0
        self.jong = 0

def ComposeChar(info): 
    if( info.cho == 0 ):
        return ""
    elif( info.jung == 0 ):
        c = str(unichr(info.cho).encode("utf-8"))
        info.cho = 0
        return c
    else:
        c = str(unichr(UniCodeHangulBase + ((choSet.index(info.cho))*21*28) +
                    (jungSet.index(info.jung))*28 + jongSet.index(info.jong)).encode("utf-8"))
        info.cho = 0
        info.jung = 0
        info.jong = 0
        return c

def composer(string):
    t = []
    current = info()
    for i in range(len(string)):
        byte = int([hex(ord(c)) for c in string[i]][0],16)
        flag = False
        if (jungTbl[0] <= byte) and (byte <= jungTbl[-1]):
            if( current.jong > 0 ) and not (current.jong in JongOnly):
                temp = current.jong
                current.jong = 0
                t.append(ComposeChar(current))
                current.cho = temp
                current.jung = byte
            elif (current.cho > 0) and (current.jung == 0) and (current.jong == 0):
                current.jung = byte
            else:
                flag = True
        elif (choTbl[0] <= byte) and (byte <= choTbl[-1]):
            if current.jong > 0:
                t.append(ComposeChar(current))
            if byte in ChoOnly :
                if( current.cho == 0 ):
                    current.cho = byte
                else:
                    flag = True
            elif byte in JongOnly:
                if (current.cho > 0) and (current.jung > 0):
                    current.jong = byte
                    t.append(ComposeChar(current))
                else:
                    flag = True
            else:
                if( current.cho == 0 ):
                     current.cho = byte
                elif (current.cho > 0) and (current.jung > 0 ):
                    current.jong = byte
                else:
                    flag = True
        else:
            flag = True
        
        if (flag) :
            t.append(ComposeChar(current))
            t.append(str(unichr(byte).encode("utf-8")))
    s = ''.join(t)
    return s


print(composer(u'ㄱㅏㄴㅏㄷㅏㅇㅗㄹㄱㅓㅅㅇㅣㅇㅘㅆ ㄱㅜㄴㅋㅋ@adgv\n'))

