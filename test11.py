user = "Shane Htet Aung"
pwd = "134570 2236"

username = input("Enter your username : ")
password = input("Enter your password : ")

if username == user and password == pwd:
    print("Hello", username)

elif username == user and password != pwd:
    print("Wrong password")

elif username != user and password = pwd:
    print("Wrong username")

elif username != user and password != pwd:
    print("Username or Password Wrong")

else:
    print("Something went wrong. Try Again")