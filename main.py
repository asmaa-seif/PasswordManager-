def decryption (password):
    epassword = ""
    for x in password:
        epassword = x + epassword
    return epassword

flag = 1
listSite = {}
while flag == 1:
    print('''
    if you want to add new site write 1
    if you want to retrive password 2, 
    if you want to end write 3''')
    option = int(input())

    if option == 1:
        site = input("enter your site name: ")
        password = input("enter your password: ")
        listSite[site] = encrypt(password)

    elif option == 2:
        targetS = input("enter your targeted site")
        pyperclip.copy(decryption(listSite.get( targetS, "not valid site ")))
        print(" password retrieved ")
    elif option == 3:
        flag = 0
        print("thank you salam ")

