class MyCalc:

    def addition(self,num1,num2):
        z= (num1 + num2)
        return z
#rk268 26 February 2023
# Here, I have done addition of 2 numbers. As expected I have taken input through a string and split it and taken the 
# input in var
# I have changed the type from string to float for the input in the main and saving the answer in the variable ans.
#  All this is done, if the input consists of a "+" in the input.
#the addtition code in main, consists of arguemnts( var[0] and var[2]) as we have to pass the split string converted into 
# float in the def addition function.
#The arguments are matched and actual addition of the numbers happens here and returned the solution to where function is called.
# If there is ans in the input then its respectively handled by passing it to var[0] or var[2] with the sign(ans or -ans) by 
# which it was entered in.

    def subtraction(self,num1,num2):
        z= (num1 - num2)
        return z
#rk268 26 February 2023
# Here, I have done subtraction of 2 numbers. As expected I have taken input through a string and split it and taken 
# the input in var.
# I have changed the type from string to float for the input in the main and saving the answer in the variable ans.
#  All this is done, if the input consists of a "-" in the input.
#the subtraction code in main, consists of arguemnts( var[0] and var[2]) as we have to pass the split string converted into 
# float in the def subtraction function.
#The arguments are matched and actual subtraction of the numbers happens here and returned the solution to where function 
# is called.
# If there is ans in the input then its respectively handled by passing it to var[0] or var[2] with the sign(ans or -ans) 
# by which it was entered in.
    def multiplication(self,num1,num2):
        z= (num1 * num2)
        return z
#rk268 26 February 2023
# Here, I have done multiplication of 2 numbers. As expected I have taken input through a string and split it 
# and taken the input in var.
# I have changed the type from string to float for the input in the main and saving the answer in the variable ans. 
# All this is done, if the input consists of a "*" in the input.
#the multiplication code in main, consists of arguemnts( var[0] and var[2]) as we have to pass the split string 
# converted into float in the def multiplication function.
#The arguments are matched and actual multiplication of the numbers happens here and returned the solution to where 
# function is called.
# If there is ans in the input then its respectively handled by passing it to var[0] or var[2] with the sign(ans or -ans) 
# by which it was entered in.
    def division(self,num1,num2):
        try:
            z= (num1 / num2)
            return z
        except ZeroDivisionError:
            print("Divide by 0 Error")
#rk268 26 February 2023
# Here, I have done division of 2 numbers. As expected I have taken input through a string and split it and 
# taken the input in var.
# I have changed the type from string to float for the input in the main and saving the answer in the variable ans. 
# All this is done, if the input consists of a "/" in the input.
#the division code in main, consists of arguemnts( var[0] and var[2]) as we have to pass the split string converted 
# into float in the def division function.
#The arguments are matched and actual division of the numbers happens here and returned the solution to where 
# function is called. Here, if the input provided consistes of 0 in the divisor(var[2]/num2,,) then this exception 
# is handled by ZeroDivisionError and none is saved in the answer.
# If there is ans in the input then its respectively handled by passing it to var[0] or var[2] 
# with the sign(ans or -ans) by which it was entered in.
            
    

    
def main():
    object = MyCalc()
    c = 0
    ans = 0
    while(True):
        var = input("please enter the expression: ").split()
        if("quit" in var or "exit" in var):
            break
        if("ans" == var[0]):
            var[0] = c
            #print(var[0])
        elif("ans" == var[2]):
            var[2] = c
        elif("-ans" == var[0]):
            
            var[0] = (-1* c)
        elif("-ans" == var[2]):
            
            var[2] = (-1* c)
#rk268 26 February 2023
        if('+' in var):
            ans = object.addition(float(var[0]),float(var[2]))
        elif('-' in var):
            ans = object.subtraction(float(var[0]),float(var[2]))
        elif('*' in var):
            ans = object.multiplication(float(var[0]),float(var[2]))
        elif('/' in var):
            if (var[1] == 0):
                print ("Divide by zero error(not a valid entry)")
            else:
                ans = object.division(float(var[0]),float(var[2]))
        
        c = ans
        print(ans)
#rk268 26 February 2023


if __name__ == "__main__":
    main()
#rk268 26 February 2023
        
