import random

def  generatePassword(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%~/abcdefghijklmnopqrstuvwxyz1234567890"
    passwords = []
    for i in length:
        password = ""
        for j in range(i):
            next_letter_index = random.randrange(len(characters))
            password = password + characters[next_letter_index]

        passwords.append(password)
    
    return passwords

def main():
    n = int(input("How many passwords do you require?: "))
    print("Generating " +str(n)+" passwords:")
    passwordLengths = []

    print("Minimum length of password should be 8")

    for i in range(n):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length<8:
            length = 8
        passwordLengths.append(length)
    
    
    Password = generatePassword(passwordLengths)

    for i in range(n):
        print ("Password #"+str(i+1)+" = " + Password[i])

main()