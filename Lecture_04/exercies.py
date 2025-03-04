# Lecture 7 questions
'''
# A1
list = []

while len(list) < 10:
    num = input('Enter a number (hit Enter when done): ')
    num = float(num)
    list.append(num)


print('\nOur list are:')
for number in list:
    print(number * 2)

# A2

my_words=["sahara", "gobi", "patagonia", "kalahari"]

for word in my_words:
    print(word.capitalize())




# A3 & A4


my_list_of_lists = [["a","b","c"], ["d","e","f"]]

for sublist in my_list_of_lists:
    for index in sublist:
        print(index)

'''

# P4
userInput = []

while len(userInput) < 3:
    userInput.append(input("Enter a firstname "))

print(userInput)