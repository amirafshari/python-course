import random

def random_guess(n=100):
    randn = random.randint(1, n)

    guess = int(input('What is your guess?'))

    while guess != randn:

        if guess > randn:
            print('Your guess is greater than my number')
        elif guess < randn:
            print('Your guess is smalelr than my number')

        guess = int(input('Guess again!'))

    print('Congrats!')

    return guess

random_guess()




###############################################################################################
###############################################################################################
###############################################################################################




def list_reverse_sum(ls1, ls2):
    ls1, ls2  = ls1[::-1], ls2[::-1]

    summation = []
    for i in range(len(ls1)):
        summation.append(ls1[i] + ls2[i])

    return summation[::-1]




def list_reverse_sum(ls1, ls2):
    ls1, ls2  = ls1[::-1], ls2[::-1]

    summation = []
    for e1, e2 in zip(ls1, ls2):
        summation.append(e1+e2)


    return summation[::-1]




def list_reverse_sum(ls1, ls2):
    ls1, ls2  = ls1[::-1], ls2[::-1]

    summation = [e1+e2 for e1, e2 in zip(ls1, ls2)]

    return summation[::-1]





###############################################################################################
###############################################################################################
###############################################################################################



def average(ls1, ls2):

    ls1 = [i for i in range(1, 14)]
    ls2 = [i for i in range(1, 20, 3)]
    ls3 = ls1 + ls2


    summation = 0
    for e  in ls3:
        summation += e

    average = summation / len(ls3)

    return average