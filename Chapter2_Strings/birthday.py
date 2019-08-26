"""Use method "str()" to translate number into string"""

age = 23
#message = "Happy " + age + "rd Birthday!"                    #wrong
message = "Happy " + str(age) + "rd Birthday!"               #correct

print(message)