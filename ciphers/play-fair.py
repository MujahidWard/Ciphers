import itertools


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
        print("decoding...")
        get_c()
    else:
        print("In this script there is two choices"
              "\n[ed] is the command for encoding a message"
              "\n[de] is the command for decoding a message\n")
        starter()
    get_kw()
    matrix_fixer()
    if startup in ed:
        encoder()
    elif startup in de:
        decode()


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
    p_fixing()


# the method for removing duplicate characters #
def remove_duplicate():
    global kw
    index = 0
    l = len(kw)
    for i in range(0, l):
        for j in range(0, i + 1):
            if kw[i] == kw[j]:
                break
        if i == j:
            kw[index] = kw[i]
            index += 1
    kw = kw[:index]


def p_fixing():
    global p
    n = 0
    while n < len(p):
        l1 = p[n]
        if n == len(p) - 1:
            p = p + 'x'
            n += 2
            continue
        l2 = p[n + 1]
        if l1 == l2:
            p = p[:n + 1] + "x" + p[n + 1:]
        n += 2
    print(f"your message after fixing: {p}")


def get_c():
    global c
    c = input("Please enter your cipher text: ")
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
    kw = input("\nPlease enter your key [word]: ")

    # for loop: to correct the input #
    for i in kw:
        if i.isupper():
            print("NO: upper letters or punctuation or numbers or space")
            get_kw()
        elif not i.isalpha():
            print("NO: upper letters or punctuation or numbers or space")
            get_kw()
    kw_fixer()


# a method to fix the key word #
def kw_fixer():
    global kw
    kw = list(map(str, kw))
    ij = ["i", "j"]
    x = 0
    while x < len(kw):
        if kw[x] in ij:
            kw[x] = "i"
        x += 1
    remove_duplicate()
    kw_read = "".join(kw)
    print(f"your key word after fixing: {kw_read}\n")


# a method to make and fix the matrix #
def matrix_fixer():
    global after_alpha
    global final_matrix
    global matrix
    after_removal = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p",
                     "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # making the encoded matrix #
    after_alpha = []

    # for loop to add every element in kw to the empty list #
    for i in kw:
        after_alpha.append(i)

    # for loop to remove used elements #
    after_removal = [x for x in after_removal if x not in kw]

    # for loop to add the rest of the letters
    for i in after_removal:
        after_alpha.append(i)

    matrix = after_alpha
    final_matrix = []
    lists1 = []
    n = 0
    while n < 5:
        if len(after_alpha) > 0:
            lists1.append(after_alpha[n])
            n += 1
            if n == 5:
                final_matrix.append(list(lists1))
                after_alpha = [x for x in after_alpha if x not in lists1]
                lists1.clear()
                n -= 5
        else:
            n = 7
    print("and your alphabet after rearranging: ")
    for i in final_matrix:
        print(f"{i}")


def slicer(seq, size):
    it = iter(seq)
    while True:
        slice_for_p = tuple(itertools.islice(it, size))
        if not slice_for_p:
            return
        yield slice_for_p


def encoder():
    ciphertext = ""
    for char1, char2 in slicer(p, 2):
        row1, col1 = divmod(matrix.index(char1), 5)
        row2, col2 = divmod(matrix.index(char2), 5)

        if row1 == row2:
            ciphertext += matrix[row1 * 5 + (col1 + 1) % 5]
            ciphertext += matrix[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[((row1 + 1) % 5) * 5 + col1]
            ciphertext += matrix[((row2 + 1) % 5) * 5 + col2]
        else:
            ciphertext += matrix[row1 * 5 + col2]
            ciphertext += matrix[row2 * 5 + col1]

    ciphertext = list(map(str, ciphertext))
    copy_c = "".join(ciphertext)
    print(f"\nyour message after encryption: {ciphertext}\n"
          f"for copy: {copy_c}")

    loop = input("again? [Yes]/[No]: \n")
    while 1:
        if loop in yes:
            starter()
        else:
            exit()


def decode():
    plaintext = ""

    for char1, char2 in slicer(c, 2):
        row1, col1 = divmod(matrix.index(char1), 5)
        row2, col2 = divmod(matrix.index(char2), 5)

        if row1 == row2:
            plaintext += matrix[row1 * 5 + (col1 - 1) % 5]
            plaintext += matrix[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[((row1 - 1) % 5) * 5 + col1]
            plaintext += matrix[((row2 - 1) % 5) * 5 + col2]
        else:
            plaintext += matrix[row1 * 5 + col2]
            plaintext += matrix[row2 * 5 + col1]

    plaintext = list(map(str, plaintext))
    p_copy = "".join(plaintext)
    print(f"\nyour ciphertext after decoding: {plaintext}\n"
          f"for coping: {p_copy}")

    loop = input("again? [Yes]/[No]: \n")
    while 1:
        if loop in yes:
            starter()
        else:
            exit()


starter()
