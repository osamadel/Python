# low = 0
# high = 100
# ans = (low + high) / 2
#
# print("Please think of a number between 0 and 100!")
# print("Is your secret number " + str(ans) + "?")
# x = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate \
# the guess is too low. Enter 'c' to indicate I guessed correctly.")
#
# while x != 'c':
#     if x == 'h':
#         high = ans
#     elif x == 'l':
#         low = ans
#     elif x != 'c':
#         print("Sorry, I did not understand your input.")
#     ans = (low + high) / 2
#     print("Is your secret number", ans, "?")
#     x = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate \
#                 the guess is too low. Enter 'c' to indicate I guessed correctly.")
#
# print ("Game over. Your secret number was: " + str(ans))

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    length = len(aStr)
    index = length//2
    if length != 0:
        if aStr[index] == char: return True
        elif aStr[index] > char and length != 1: return isIn(char, aStr[:index])
        elif aStr[index] < char and length != 1: return isIn(char, aStr[index:])
        else: return False

print isIn('l', 'l')