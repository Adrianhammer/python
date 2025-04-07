#Oppgave 1

import random


def generate_password():
    password_length = int(input("Give a number between 15 and 20 to decide the length of your password"))
    password = ""
    characters = (r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRZTUVWXYZ!@#-_.,:;()=?\/")
    if password_length < 15 or password_length > 20:
        password_length = int(input("Invalid! Enter a number between 15 and 20: "))
    else:
        True
        
    for i in range(password_length):
        password += random.choice(characters)
   #slet med å finne filen og om den ble lagd     
    with open("password.txt", "w") as file:
        file.write(f"This is your password: {password}")

        print(password)
    
generate_password()