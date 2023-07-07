"""
This is a game which is play with you guessing numbers
"""

import random

def sontop(x=10):
    tasodifiy = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim, topa olasizmi? ")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy:
            print("Xato. Men O'ylagan son bundan kattaroq. Harakat qilib ko'ring")
        elif taxmin > tasodifiy:
            print("Xato. Men o'ylagan son bundan kichikiroq. Yana harakat qilib ko'ring")
        else:
            break
    print(f"Tabriklaymiz. {taxminlar} taxmin bilan topdingiz!")
    return taxminlar

def sontoppc(x=10):
    input(f"Men 1 dan {x} gacha son o'ylang va istalgan tugmani bosing")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ro (t)"
                      f"Men o'ylagan son bundan katatroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} taxmin bilan topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontoppc(x)
        if taxminlar_user>taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_pc>taxminlar_user:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi? ha(1)/yo'q(0): "))

play()