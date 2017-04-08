# # # bobobbobobwobbvoboboalbobboobbobob
# s = 'abcdefghijklmnopqrstuvwxyz'
# max = 0
# c = 0
# sub = ""
# start_index = 0
# if len(s) != 0:
#     for i in range(len(s)-1):
#         if s[i] > s[i+1]:
#             c = len(s[start_index:i+1])
#             if max < c:
#                 max = c
#                 sub = s[start_index:i+1]
#             c = 0
#             start_index = i+1
#     if not sub:
#         sub = s
# print sub

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) >= epsilon:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))