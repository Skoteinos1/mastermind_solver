# Mastermind Solver
Helps to solve mastermind game.

It is not that hard to solve, but I thought it would be nice project, program that can solve this game.

It is very simple, it generates all possible combinations. if you enter your guess and its result, it will print you out all remaining possible combination.
Repeat until game is solved.

Steps which I used to solve game on picture:
remaining_options = remove_wrong_possibilities((('pu', 'or', 'bl', 'ye'), (0, 1)))
remaining_options = remove_wrong_possibilities((('re', 'br', 'gr', 'pi'), (0, 3)))
remaining_options = remove_wrong_possibilities((('br', 'pi', 'pu', 'gr'), (2, 1)))
remaining_options = remove_wrong_possibilities((('br', 'pu', 're', 'gr'), (2, 1)))
