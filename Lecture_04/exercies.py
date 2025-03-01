# Lecture 7 questions

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

# A3

my_list_of_lists = [["a","b","c"], ["d","e","f"]]

for n in my_list_of_lists:
    print(my_list_of_lists)
