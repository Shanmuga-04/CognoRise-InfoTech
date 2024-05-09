import random

password=int(input("Enter the length of the password:"))
c="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
output="".join(random.sample(c,password))
print(output)
