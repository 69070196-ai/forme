""" Caesar salad """
def cipher(message):
    """ + 1 """
    toAppend = ""
    for i, j in enumerate(message):
        for k in j:
            num = ord(k)
            if k.isalpha():
                if k.isupper():
                    num = (num - 65 + 1) % 26 + 65
                else:
                    num = (num - 97 + 1) % 26 + 97
            toAppend += chr(num)
        message[i] = toAppend
        toAppend = ""
    return message

def decode():
    """ decode the word """
    message = input().split()
    usual_word = ("what", "when", "why", "which", "this", "there",
                  "where", "the", "is", "am", "are", "you", "we", 
                  "they", "he", "she", "it")
    while True:
        found = False

        for i in message:
            if i.lower() in usual_word:
                found = True

        if found:
            break

        message = cipher(message)

    print(" ".join(message))
decode()
