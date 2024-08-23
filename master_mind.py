def penalty2(j):
    '''
    [list] -> Boolean
    j is a list that we compare with colours list to make sure the
    user doesn't put any strings not included in the list of colours.
    Returns False if it violated the rule.
    '''
    colours2 = []
    for g in colours:
        colours2.append(g.upper())

    
    for T in j:
        if T.upper() not in colours2:
            return False
            break
        else:
            continue

    return True

def penalty3(p):
    '''
    [list] -> Boolean
    p is a list that we compare with colours list to make sure the
    user doesn't put any repeated strings.
    Returns False if it violated the rule.
    '''
    guess2 = []
    for m in p:
        guess2.append(m.upper())
        
    for y in guess2:
        if guess2.count(y)>1:
            return False
            break
        else:
            continue
    return True

################## Main part of code ######################
import random
colours = ['Red', 'Yellow', 'Blue', 'Green', 'Orange', 'Pink', 'Purple', 'Cyan', 'Silver', 'Teal']
code = []
Penalties = 0
name = str(input('What is your name? '))
print('Welcome to Master Mind', name + '!')
print('The code maker is here. Available colors are')

for i in colours:
    if i != colours[-1]:
        print(i + ', ', end = '')
    else:
        print(i)

print('You have 15 guesses, total of 5 penalties are allowed but avoid penalties.')
print('The code maker selected 4 colors.')
print('You can start guessing', name+ '.')

while len(code) != 4:
    o = colours[random.randint(0, 9)]

    if o not in code:
        code.append(o)

##Guessing part with penalties
        
for j in range(1, 16): 
    Blacks = 0
    Whites = 0
    
    print('Enter guess number', str(j)+':', end = ' ')

    w = str(input())

    guess = w.split()

    if len(guess)!=4:
        if not penalty2(guess) and not penalty3(guess):
            print('Sorry', name +',', 'you need to enter at least 4 colors for each guess. Also, cannot recognize the colors you entered and repeated colors are not allowed in this game. One penalty is considered.')

            Penalties += 1

            print('Total penalties =', Penalties)
            
            if Penalties == 5:
                print(name + ',', 'you lost the game by reaching the maximum number of allowed penalties.')
                break
        
        elif not penalty2(guess) and penalty3(guess):
            print('Sorry', name +',', 'you need to enter at least 4 colors for each guess. Also, cannot recognize the colors you entered. One penalty is considered.')

            Penalties += 1

            print('Total penalties =', Penalties)

            if Penalties == 5:
                print(name + ',', 'you lost the game by reaching the maximum number of allowed penalties.')
                break

        elif not penalty3(guess) and penalty2(guess):
            print('Sorry', name +',', 'you need to enter at least 4 colors for each guess. Also, repeated colors are not allowed in this game. One penalty is considered.')

            Penalties += 1

            print('Total penalties =', Penalties)
            if Penalties == 5:
                print(name + ',', 'you lost the game by reaching the maximum number of allowed penalties.')
                break
            
        else:
            print('Sorry', name +',', 'you need to enter at least 4 colors for each guess. One penalty is considered.')

            Penalties += 1

            print('Total penalties =', Penalties)
            if Penalties == 5:
                print(name + ',', 'you lost the game by reaching the maximum number of allowed penalties.')
                break

    
    elif not penalty2(guess):
        if not penalty3(guess):
            print('Sorry', name +',', 'cannot recognize the colors you entered. Also, repeated colors are not allowed in this game. One penalty is considered.')

            Penalties += 1

            print('Total penalties =', Penalties)

            if Penalties == 5:
                print(name + ',', 'you lost the game by reaching the maximum number of allowed penalties.')
                break
        else:
            print('Sorry', name +',', 'cannot recognize the colors you entered. One penalty is considered.')

            Penalties += 1

            print('Total penalties =', Penalties)

            if Penalties == 5:
                print(name + ',', 'you lost the game by reaching the maximum number of allowed penalties.')
                break

    
    elif not penalty3(guess):
        print('Sorry', name +',', 'repeated colors are not allowed in this game. One penalty is considered.')

        Penalties += 1

        print('Total penalties =', Penalties)

        if Penalties == 5:
            print(name + ',', 'you lost the game by reaching the maximum number of allowed penalties.')
            break

    else:
        code2 = []
        for A in code:
            code2.append(A.upper())

        guess2 = []
        for B in guess:
            guess2.append(B.upper())
            
        if guess2 == code2:
            print('You got 4 blacks', name + '.')
            print('You won the game with', str(j), 'guess(es) and', str(Penalties), 'penalties, Congratulations.')
            break

        for H in guess2:
            if H == code2[guess2.index(H)]:
                Blacks += 1
            elif H in code2:
                Whites += 1
        print('You got', Blacks, 'black(s), and', Whites, 'white(s) for this guess.')
        if j == 15:
            print('Sorry', name + ',', 'you ran out of guesses and you lost the game with', str(Penalties), 'penalties.')
            
