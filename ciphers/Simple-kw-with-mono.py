# caller method
def starter():
    global ed
    global startup
    startup = input("please enter [ed] / [de] / [help]: ")
    ed = ["ed", "ED", "Ed", "eD"]
    de = ["de", "DE", "De", "dE"]
    if startup in ed:
        print("encoding...\n")
        get_p()
    elif startup in de:
        print("decoding...\n")
        get_c()
    else:
        print("In this script there is two choices"
              "\n[ed] is the command for encoding a message"
              "\n[de] is the command for decoding a message\n")
        starter()
    get_kw()
    remove_duplicate()
    encode()
    if startup in de:
        decoding()
    again()


def get_p():
    global p
    p = input("Please enter your word to encode: ")

    # for loop: to correct the input #
    for i in p:
        if i.isupper():
            print("NO: upper letters or punctuation or numbers or space")
            get_p()
        elif not i.isalpha():
            print("NO: upper letters or punctuation or numbers or space")
            get_p()


def get_c():
    global c
    c = input("Please enter your cipher text to decode: ")

    # for loop: to correct the input #
    for i in c:
        if i.isupper():
            print("NO: upper letters or punctuation or numbers or space")
            get_c()
        elif not i.isalpha():
            print("NO: upper letters or punctuation or numbers or space")
            get_c()


def get_kw():
    global kw
    kw = input("Please enter your key [word]: ")

    # for loop: to correct the input #
    for i in kw:
        if i.isupper():
            print("NO: upper letters or punctuation or numbers or space")
            get_kw()
        elif not i.isalpha():
            print("NO: upper letters or punctuation or numbers or space")
            get_kw()


# the method for removing duplicate characters #
def remove_duplicate():
    global kw
    kw = list(kw)
    index = 0
    l = len(kw)
    for i in range(0, l):
        for j in range(0, i + 1):
            if kw[i] == kw[j]:
                break
        if i == j:
            kw[index] = kw[i]
            index += 1
    kw = "".join(kw[:index])


# encoding method #
def encode():
    global replaceable
    global small_alpha
    small_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                   "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    after_removal = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                     "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    replaceable = []

    # for loop to remove the kw letters from the alphabet #
    after_removal = [i for i in after_removal if i not in kw]

    # for loop to append every letter in kw to the empty list #
    for i in kw:
        replaceable.append(i)

    # for loop to append every letter in after_removal to the replaceable list #
    for i in after_removal:
        replaceable.append(i)

    print(f"\n{small_alpha} \n{replaceable}\n")

    if startup in ed:
        # for loop to get the indexes of the message to replace it later #
        p_indexes = []
        for i in p:
            n = small_alpha.index(i)
            p_indexes.append(n)

        # for loop to replace the indexes from the message with the encoded alpha #
        c_encode = []
        for i in p_indexes:
            c_encode.append(replaceable[i])
        c_copy = "".join(c_encode)
        print(f"your message after encode: {c_encode}\n"
              f"or for coping: {c_copy}")


# decoding method #
def decoding():
    c_indexes = []

    # for loop to get the indexes for c #
    for i in c:
        n = replaceable.index(i)
        c_indexes.append(n)
    c_decode = []

    # for loop to replace indexes in c_indexes with characters from small_alpha #
    for i in c_indexes:
        c_decode.append(small_alpha[i])

    c_decode_copy = "".join(c_decode)

    print(f"your message after decode: {c_decode}\n"
          f"for copy: {c_decode_copy}")


# looping the script #
def again():
    yes = ["Yes", "Y", "yes", "y"]
    loop = input("again? [Yes]/[No]: \n")
    if loop in yes:
        starter()
    else:
        exit()


starter()
