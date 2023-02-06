a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]

#UCID rk268 date:2/5/2023
def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # TODO add new code here to print the desired result
    for i in range(0,len(arr)):
        abcd=0
        if(type(arr[i])==str):
            if(int(arr[i])<0):
                abcd=int(arr[i])*(-1)
                abcd=str(abcd)
                print('\'{}\''.format(abcd), end=" ")
            else:
                print(str('\'{}\''.format(arr[i])), end=" ")
        elif(type(arr[i]==int)):
            if(arr[i]<0):
                abcd=arr[i]*(-1)
                print(abcd, end=" ")
            else:
                print(arr[i], end=" ")
        else:
            if(arr[i]<0):
                abcd=arr[i]*(-1)
                print(abcd, end=" ")
            else:
                print(arr[i], end=" ,")
print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)