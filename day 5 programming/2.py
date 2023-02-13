grade=(input("enter the grade of the employee:"))
salary=int(input("enter the employee salary:"))
if(salary<=0):
    bonus=0
    print("enter the correct salary")
elif(grade=="A" ):
    bonus=5/100*salary
    print(bonus)
    print(bonus+salary)
elif(grade=="B"):
    bonus=10/100*salary
    print(bonus)
    print(bonus+salary)
elif(salary<=10000):
    bonus2=bonus+2/100*salary
    print(bonus2)
    print(bonus+salary)
elif(salary<=0):
    print("enter the correct salary")
   
else:
    print("incorrect input")
