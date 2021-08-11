import tkinter
import random

root = tkinter.Tk()
root.title("Rock,Paper,Scissors")
root.geometry("400x500")

random_number = random.randit(1, 3)
if random_number == 1:
    computer_choice = "R"
elif random_number == 2:
    computer_choice = "P"
elif random_number == 3:
    computer_choice = "S"


def rock():
    label_user_choice['text'] = "ROCK"

    # Choices
    if computer_choice == "R"
        label_result['text'] = "TIE"
        label_computer_choice['text'] = "ROCK"
    elif computer_choice == "P"
        label_result['text'] = "Computer wins"
        label_computer_choice['text'] = "PAPER"
    elif computer_choice == "S"
        label_result['text'] = "Player wins"
    label_computer_choice['text'] = "SCISSORS"


def paper():
    label_user_choice['text'] = "PAPER"
    # Choices
    if computer_choice == "P"
        label_result['text'] = "TIE"
        label_computer_choice['text'] = "PAPER"
    elif computer_choice == "S"
        label_result['text'] = "Computer wins"
        label_computer_choice['text'] = "SCISSORS"
    elif computer_choice == "R"
        label_result['text'] = "Player wins"
    label_computer_choice['text'] = "ROCK"


def scissors():
    label_user_choice['text'] = "SCISSORS"
    # Choices


if computer_choice == "S"
    label_result['text'] = "TIE"
    label_computer_choice['text'] = "SCISSORS"
elif computer_choice == "R"
    label_result['text'] = "Computer wins"
    label_computer_choice['text'] = "ROCK"
elif computer_choice == "P"
    label_result['text'] = "Player wins"
label_computer_choice['text'] = "PAPER"


def result():
    global computer_choice
    random_number = random.randit(1, 3)
    if random_number == 1:
        computer_choice = "R"
    elif random_number == 2:
        computer_choice = "P"
    elif random_number == 3:
    computer_choice = "S"

    label_computer_choice['text'] = ""
    label_user_choice['text'] = ""
    label_result_choice['text'] = "Choose"


label_result = tkinter.Label(root, text="choose")
label_result.pack()

button_rock = tkinter.Button(root, text="Rock", command=rock)
button_rock.pack()

button_paper = tkinter.Button(root, text="Paper", command=paper)
button_paper.pack()

button_scissors = tkinter.Button(root, text="Scissors", command=rock)
button_scissors.pack()

label_computer = tkinter.Label(root, text="")
label_computer.pack()

label_user = tkinter.Label(root, text="")
label_user.pack()

button_reset = tkinter.Button(root, text="Reset", command=reset)
button_reset.pack()

root.mainloop()
