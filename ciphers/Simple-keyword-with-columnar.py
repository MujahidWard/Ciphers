# the calling method #
def starter():
    global startup
    global ed
    global yes
    ed = ["ed", "Ed", "ED", "eD"]
    de = ["de", "De", "DE", "dE"]
    yes = ["Yes", "Y", "yes", "y"]
    startup = input("please enter [ed] / [de] / [help]: ")
    # the if statement for encoding or decoding #
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
    get_k_word()
    remove_duplicate()
    replacement()


# the method for value message #
def get_p():
    global p
    p = input("please input your word to encode: ")
    for i in p:
        if i.isupper():
            print("NO: upper letters or punctuation or numbers or space")
            get_p()
        elif not i.isalpha():
            print("NO: upper letters or punctuation or numbers or space")
            get_p()


# the method for value encoded message #
def get_c():
    global c
    c = input("please input your encoded message to decode: ")
    for i in c:
        if i.isupper():
            print("NO: upper letters or punctuation or numbers or space")
            get_c()
        elif not i.isalpha():
            print("NO: upper letters or punctuation or numbers or space")
            get_c()


# the method for value key word #
def get_k_word():
    global kw
    kw = input("please enter your key word: ")
    for i in kw:
        if i.isupper():
            print("NO: upper letters or punctuation or numbers or space")
            get_k_word()
        elif not i.isalpha():
            print("NO: upper letters or punctuation or numbers or space")
            get_k_word()


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


# the method for shifting and getting indexes #
def replacement():
    small_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                   "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if startup in ed:
        # for loop to get plaintext indexes in alphabet #
        p_indexes = []
        for i in p:
            n = small_alpha.index(i)
            p_indexes.append(n)

    # removing kw from alphabet #
    after_removal = [x for x in small_alpha if x not in kw]

    # while loop to create empty lists equal to kw length #
    lists = []
    for i in range(len(kw)):
        empty = []
        lists.append(empty)

    # while loop to add kw elements to the empty lists #
    n = 0
    while n < len(kw):
        lists[n].append(kw[n])
        n += 1

    # while loop to add alphabet elements to kw lists #
    n = 0
    while n < len(kw):
        l = 0
        while l < len(after_removal):
            if n == len(kw):
                n = 0
            lists[n].append(after_removal[l])
            n += 1
            l += 1
        n += 100

    # for loop to rearrange every list in lists to new alpha #
    new_alpha = []
    for i in lists:
        for j in i:
            new_alpha.append(j)

    if startup in ed:
        # for loop to get cipher text from new alpha #
        cipher_text = []
        for i in p_indexes:
            n = new_alpha[i]
            cipher_text.append(n)
        for_copy = "".join(cipher_text)

        # outputs #
        print(f"\nthe alphabet = {small_alpha}")
        print(f"new alphabet = {new_alpha}")
        print(f"\nyour cipher text = {cipher_text}\n"
              f"for copy = {for_copy}")
    else:
        # for loop to get cipher text indexes #
        c_indexes = []
        for i in c:
            n = new_alpha.index(i)
            c_indexes.append(n)

        # for loop to decode cipher text #
        plain_text = []
        for i in c_indexes:
            n = small_alpha[i]
            plain_text.append(n)
        for_copy = "".join(plain_text)

        # outputs #
        print(f"\nthe alphabet = {small_alpha}")
        print(f"new alphabet = {new_alpha}")
        print(f"\nyour cipher text = {plain_text}\n"
              f"for copy = {for_copy}")

    # looping the script #
    loop = input("\nagain? [Yes]/[No]: \n")
    n = 0
    while n == 0:
        if loop in yes:
            starter()
        else:
            exit()


starter()
