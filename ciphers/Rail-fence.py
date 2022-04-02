# starter method #
def starter():
    get_p()
    get_d()
    encode()


# getting the value of the message to encode #
def get_p():
    global p
    p = input("Please input your message to encode: ")


# getting the value of the depth #
def get_d():
    global d
    d = int(input("Please input the depth: "))
    if d > len(p):
        print("The depth should be equal or less than the length of the message!")
        get_d()
    elif d == 0:
        print("Depth can't be equal to zero!")
        get_d()
    print("")


# rail encoding #
def encode():
    # for loop to create empty lists #
    empty_lists = [[" " for i in range(len(p))] for j in range(d)]
    flag = 0
    row = 0

    # for loop to arrange p elements in the empty lists rail_fence style #
    for i in range(len(p)):
        empty_lists[row][i] = p[i]
        if row == 0:
            flag = 0
        elif row == d - 1:
            flag = 1
        if flag == 0:
            row += 1
        else:
            row -= 1

    # While loop to print empty lists elements without [", ', ., /, {, }, (, )] #
    x = d - 1
    while x >= 0:
        print("".join(empty_lists[x]))
        x -= 1
    print("")
    # for loop to add any element in empty lists to cipher text list to print it without spaces #
    cipher_text = []
    m = d - 1
    while m >= 0:
        n = 0
        while n < len(p):
            if empty_lists[m][n] != ' ':
                cipher_text.append(empty_lists[m][n])
            n += 1
        m -= 1
    for_copy = "".join(cipher_text)
    print("Cipher Text: ", for_copy)

    yes = ["Yes", "Y", "yes", "y"]
    again = input("again? [Yes]/[No]: ")
    if again in yes:
        starter()
    else:
        exit()


starter()
