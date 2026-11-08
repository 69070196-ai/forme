""" Stupidy AI! """
def cleaned(text):
    """ cleaned word """

    cleaned_word = "".join(char for char in text if char.isalpha())

    return cleaned_word

def num_check(text):
    """ is there a number """
    check = False
    for i in text:
        if i.isdigit():
            check = True
    return check

def ai_bot():
    """ Prepared message set """
    num = int(input())
    message_list = []

    for _ in range(num):
        message = input()
        message_list.append(message.lower().split())

    for message in message_list :
        message_length = 0
        else_check = True
        for i in message:
            print(i)
            message_length += len(i)
        for text in message:
            if cleaned(text) == "hi" or cleaned(text) == "hello":
                print("Hello! How can I help you?")
                else_check = False
                break
            if cleaned(text) == "bye" or cleaned(text) == "goodbye":
                print("Goodbye! Have a nice day!")
                else_check = False
                break
            if "?" in text:
                print("That's an interesting question!")
                else_check = False
                break
            if num_check(text):
                print("I see some numbers there!")
                else_check = False
                break
            if message_length > 20:
                print( "That's quite a long message!")
                else_check = False
                break
        if else_check:
            print("I understand.")
ai_bot()
