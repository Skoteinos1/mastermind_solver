import itertools


def remove_wrong_possibilities(guess):
    global possible
    options = possible

    for i in range(len(options)-1, -1, -1):
        if evaluate(options[i], guess[0]) != guess[1]:
            options.pop(i)
    return options


def evaluate(original, guess):
    original = list(original)
    guess = list(guess)
    black = 0
    white = 0
    for i in range(4):
        if original[i] == guess[i]:
            black += 1
    
    for i in range(4):
        if guess[i] in original:
            white += 1
            original.remove(guess[i])
    return black, white - black
    

stuff = ['pu', 'or', 'bl', 'ye', 're', 'br', 'gr', 'pi']
possible = []
for subset in itertools.product(stuff, repeat=4):
    possible.append(subset)

# print(possible)
# print(len(possible))

# possible = remove_wrong_possibilities((('', '', '', ''), (0, 2)))
possible = remove_wrong_possibilities((('pu', 'or', 'bl', 'ye'), (0, 1)))
possible = remove_wrong_possibilities((('re', 'br', 'gr', 'pi'), (0, 3)))
possible = remove_wrong_possibilities((('br', 'pi', 'pu', 'gr'), (2, 1)))
possible = remove_wrong_possibilities((('br', 'pu', 're', 'gr'), (2, 1)))
# possible = remove_wrong_possibilities((('br', 'ye', 'gr', 'ye'), (0, 1)))

print(possible)
