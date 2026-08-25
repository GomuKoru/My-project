print("/n===LOGIN===")
username = "Faiz"
password = 6789

while True:
    input_username = str(input("Input you username: "))
    
        
    if input_username == username:
        print("CORRECT")
        break
    
    else:
        print("INCORRECT USERNAME!!!")
    
    
while True:
    input_password = int(input("Input you password: "))
    
    if input_password == password:
        print("CORRECT")
        break
        
    else:
        print("WRONG PASSWORD!!!")
    
    
print('Welcome', username, '!!!!')