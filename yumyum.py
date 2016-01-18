print("Hey there! Would you want to try some local food? Choose from the list below:\n1. Nasi Lemak\n2. Chicken Rice\n3. Roti Prata\n4. Hokkien Mee")
data = int(input("So, what would you like? Please enter the option number."))
if data == 1:
  print("That will be $1.50!")
elif data == 2:
  print("That will be $2.00!")
elif data == 3:
  print("That will be $1.00!")
elif data == 4:
  print("That will be $3.00!")
else:
  print("Sorry, we do not have that option:(")
