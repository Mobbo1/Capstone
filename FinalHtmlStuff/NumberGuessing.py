import statistics
number_list = []
number_of_guesses = 0
def create_list():
    for x in range(0,101,1):
        number_list.append(x)
    

create_list()

correct_number = int(input("Please think of a number in your head"))

guess_status = False

list_length = len(number_list)

def remove_up_to(list,number):
    for x in range(number):
        del list[x]


def remove_higher(list,number):
    for number  in range(number,list_length):
        print("List length is " + str(list_length) + "") 
        print(number)
        
        del list[list.index(number)]


while guess_status == False :
    number_of_guesses +=1
    number_guessed = statistics.median(number_list)

    if number_guessed != correct_number:
        print(number_guessed)
        adjustment = int(input("Is our number higher or lower, 0 = higher, 1 = lower"))
        if adjustment == 0:
            remove_up_to(number_list,number_guessed)
        else:
            remove_higher(number_list,number_guessed)
        
    else:
        guess_status = True
        print("Congrats")



# 0 = higher, 1 = lower

