from listas import leet_basic, leet_deep


# Let's code and decode in 1337!

def encode(level, message):
    encodemessage = []

    message = message.upper()

    if level == 1:
        mensagem = list(message)
        level = "B451C"
        for l in mensagem:
            if l in leet_basic.keys():
                encodemessage.append(leet_basic[l])
            else:
                encodemessage.append(l)
    else:
        mensagem = list(message)
        level = "C0MPL3T3"
        for l in mensagem:
            if l in leet_deep.keys():
                encodemessage.append(leet_deep[l])
            else:
                encodemessage.append(l)

    encodemessage = "".join(encodemessage)

    return level, encodemessage


def decode(level, message):
    decodemessage = []

    message = message.upper()

    if level == 1:
        mensagem = list(message)
        level = "B451C"
        for l in mensagem:
            found = False
            for chave, valor in leet_basic.items():
                if valor == l:
                    decodemessage.append(chave)
                    found = True
                    break
            if not found:
                decodemessage.append(l)
    else:
        mensagem = message.split()
        print(mensagem)
        level = "C0MPL3T3"
        for l in mensagem:
            found = False
            for chave, valor in leet_deep.items():
                if valor == l:
                    decodemessage.append(chave)
                    found = True
                    break
            if not found:
                decodemessage.append(l)

    decodemessage = "".join(decodemessage)

    return level, decodemessage


opt = None

while opt != 3:
    opt = int(input("\n3NC0D3[1] 0R D3C0D3[2] 0R 3X17[3]: "))

    if opt == 1:
        print("3NC0D3 L3V3L:")
        level = int(input("B451C[1] 0R C0MPL3T3[2]: "))
        message = input("M355463: ")
        retorno = encode(level, message)
        print(f"Mensagem Codificada - Level[{retorno[0]}]: {retorno[1]}")
    elif opt == 2:
        print("[!] USE SPACE BETWEEN LETTERS! [!]")
        print("D3C0D3 L3V3L:")
        level = int(input("B451C[1] 0R C0MPL3T3[2]: "))
        message = input("M355463: ")
        retorno = decode(level, message)
        print(f"Mensagem Decodificada - Level[{retorno[0]}]: {retorno[1]}")
    elif opt == 3:
        print("G00DBY3! ", end="")
    else:
        print("7H15 0P710N D0N'7 3X157! 7RY 4641N!")

print("7H4NK5 F0R U5E!\n4CC355 -> https://github.com/titiomathias")
