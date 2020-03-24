print("Welcome...")
Welcome=input("Do you have an account?y/n:")
if Welcome=="n":
    while True:
        username=input("Enter a username:")
        password=input("Enter a password:")
        password1=input("Enter confirm password:")
        if password==password1:
            file=open(username+".text","w")
            file.write(username+":"+password)
            file.close()
            welcome="y"
            break
        print("Password donot match!")

if welcome == "y":
   while True:
       login1=input("Login:")
       login2=input("Password:")
       file=open(login1+".txt","r")
       data=file.readline()
       file.close()
       if data==login1+":"+login2:
           print("Welcome")
           break
       print("Incorrect username or password.")