dic = {1: "kilometers into meters", 2: "meters into meters", 3: "centimeters into meters", 4: "milimeters into meters"}
for i in dic:
    print(str(i) + ": " + dic[i])
print("Enter your choice: ", end = '')
user_choice = int(input())
print("Enter value you want to convert: ", end = '')
value = float(input())
if (user_choice == 1):
    print("%.3f kilometers after convert into meters = %.3f"%(value, value * 1000))
elif (user_choice == 2):
    print("%.3f meters after convert into meters = %.3f"%(value, value))
elif (user_choice == 3):
    print("%.3f centimeters after convert into meters = %.3f"%(value, value / 100))
elif (user_choice == 4):
    print("%.3f milimeters after convert into meters = %.3f"%(value, value / pow(10, 3)))
else:
    print("Your choice is invalid.")
