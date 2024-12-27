## Input Validation (garbage in, garbage out, GIGO)

score = int(input('Enter a test score: '))          # priming read

while score < 0:                                    # validate the input
    print('ERROR: The score cannot be negative.')
    score = int(input('Enter a correct score: '))
