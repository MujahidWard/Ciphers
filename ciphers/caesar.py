# the calling method #
def c_starter():
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
        de_choice = input("With key or the key is missing ^_^ ? \n"
                          "[yes] if you got the key: ")
        if de_choice in yes:
            print("decoding...\n")
            get_c()
        else:
            print("decoding...\n")
            get_c()
            decode_wk()
    else:
        print("In this script there is two choices"
              "\n[ed] is the command for encoding a message"
              "\n[de] is the command for decoding a message\n")
        c_starter()
    get_k()
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


# the method for value key #
def get_k():
    global k
    k = int(input("please input your key: "))
    while k >= 26:
        print("the key must be lower than 26")
        get_k()


# the method for shifting and getting indexes #
def replacement():
    small_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                   "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    replaceable = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                   "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
    index = []
    for i in small_alpha:
        z = small_alpha.index(i)
        index.append(z)
    # the for loop for the replacement #
    for idx, value in enumerate(index, start=k):
        replaceable[idx % len(replaceable)] = small_alpha[value]
    # if statement for dividing the encoding and decoding: {process}
    if startup in ed:
        # the for loop for the indexes in the message #
        p_index = [small_alpha.index(i) for i in p]
        # the for loop for replacing the indexes by the new letters
        for idx, value in enumerate(p_index):
            p_index[idx] = replaceable[value]
    else:
        # the for loop for the indexes in the message #
        p_index = [replaceable.index(i) for i in c]
        # the for loop for replacing the indexes by the new letters
        for idx, value in enumerate(p_index):
            p_index[idx] = small_alpha[value]
    # outputs #
    print(f"\nalphabet = {small_alpha}")
    print(f"after en = {replaceable}")
    print(f"your word after encoding = {p_index}\n")
    p_index = "".join(p_index)
    print(f"your word for coping = {p_index}")
    # looping the script #
    loop = input("again? [Yes]/[No]: \n")
    n = 0
    while n == 0:
        if loop in yes:
            c_starter()
        else:
            exit()


def decode_wk():
    small_alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                   "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    replaceable = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                   "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
    index = []
    for i in small_alpha:
        z = small_alpha.index(i)
        index.append(z)

    # the for loop for the replacement #
    n = 0
    while n < 26:
        for idx, value in enumerate(index, start=n):
            replaceable[idx % len(replaceable)] = small_alpha[value]
        # the for loop for the indexes in the message #
        p_index = [replaceable.index(i) for i in c]
        # the for loop for replacing the indexes by the new letters
        for idx, value in enumerate(p_index):
            p_index[idx] = small_alpha[value]
        print("message: ", "".join(p_index))
        y = input("input [yes] if this is your message: ")
        if y in yes:
            print("your message: ", "".join(p_index))
            n = exit()
        else:
            if n == 25:
                print("uhh! hmmmm? you passed 26 tries and didn't fined your message\n"
                      "I don't know ¯\\_(0_0)_/¯")
                exit()
            n += 1


c_starter()
