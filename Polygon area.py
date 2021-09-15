from math import tan,pi
#  طول یک ضلع : 
lenght_Sides = float(input("enter your lenght_Sides : "))
# تعداد اضلاع : 
number_Sides = float(input("enter your number_Sides : "))
# مساحت :
Area = (number_Sides *(lenght_Sides**2))/(4*tan(pi/number_Sides))
print(f"area is : {Area}")