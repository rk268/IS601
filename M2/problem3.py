a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]

#UCID-rk268 Date-2/5/2023
def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    #TODO add new code here to print the desired result
    for i in range(0,len(arr)):
        if(type(arr[i])==int):
            if(arr[i]<0):
                ans=arr[i]*(-1)
                print(ans, end=" ")
            else:
                print(arr[i], end=" ")

        elif(type(arr[i])==float):
            if(arr[i]<0):
                ans=arr[i]*(-1)
                print(ans, end=" ")
        else:
            if(type(arr[i]==str)):
                r= arr[i].replace('-', "")
                print('\'{}\''.format(r), end=" ")
                print(type(arr[i]),end=" ")
                #[print(f"{arr[i]} {type(arr[i])}, ") for i in arr]



print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
