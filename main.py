def start_game():
    print("Welcome to your very own interactive Paw patrol Adventure bay game.")
    username = input("Enter your name: ")
    Placechooser(username)


def Placechooser(username):
    choice = input("Hi " + username + " choose where you would like to explore: Barkingburg, Foggy Bottom, or Katies Pet parlor: ").lower()
    if choice == "barkingburg":
        barkingburg()
    elif choice == "foggy bottom":
        foggybottom()
    elif choice == "katies pet parlor":
        Katies_Pet_Parlor(username)
    else:
        print(choice + " isn't an options. Please pick from the three choices listed above.")
        Placechooser(username)



def Katies_Pet_Parlor(username):
    print("welcome to Katies Pet Parlor! I ma ryder and IO have chosen you to help me with this mission. "
          "Katies cat has climbed onto he roof, and sky isn't able to get her down. "
          "She says we have to answer 3 riddles of hers and then she will agree to coming down. "
          "For each question you have three tries to answer. "
          "We need your qick thinking on this mission. Please hurry!" )
    q1 = input("Here is your first riddle: 10 copycats were sitting in a car. One came out. How many are left? " ).lower()
    if q1 == "zero" or q1 == "none" or q1 == "0":
        print("Hissssss, you got this question right, here si the next question: ")
    q2 = input("I'm found in socks, scarves, and mittens. I'm found in the paws of playful kittens. What am I? ").lower()
    if q2 == "yarn" or q2 == "wool":
        print("Oh no, you got it right again! I'm not coming down dont get this next one right")
    q3 = input("How many lives does a cat have?").lower()
    if q3 == "nine" or q3 == "9":
        print("I am a cat of my word, sadly I will have to come down. Good job, I now declare you to be an honorary member of the paw patrol. " + username)
        print("You have completed your mission")

def barkingburg():
    print("welcome")

def foggybottom():
    print("welcome")


start_game()





'''

foggy bottom

, barkingburg,
 
 katies pet parlor 
 
 
 cat run away needs you to amswer qjestions fr her to come out, cat on roof of parlor 
 
 
 14. Riddle: Where did the cat go after losing its tail?
Answer: To the re-tail store.




'''
