#password generator
import random                       
  
# defining a function to randomly generate the password  
def generate_pw(length):    

    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"  
    str = ""  
  
    for i in range(length):  
        str = str + random.choice(characters)  
      
    return str
  

length = int(input("Enter the length of the desired password: "))
str = generate_pw(length)  
print("Generated Password:", str)

