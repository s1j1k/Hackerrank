# https://www.hackerrank.com/challenges/the-minion-game/problem

# note that using a single loop is better as two loops will cause timeout on larger inputs
# since any substring is accepted, you can simply add the number of possible substrings to the play score

def minion_game(string):
    string = string.lower()

    vowels = 'aeiou'

    # Stuart has substrings starting with consonant
    # Kevin has substring starting with vowel
    S = 0
    K = 0

    for i in range(len(string)):
        c = string[i]

        if c in vowels:
            # Kevin's turn
            K += (len(string)-i)
        else:
            # Stuart's turn
            S += (len(string)-i)

    # print the winner
    if K > S:
        print("Kevin",K)
    elif S > K:
        print("Stuart",S)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
