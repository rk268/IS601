a1 = [10.001, 11.591, 0.011, 5.991, 16.121, 0.131, 100.981, 1.001]
a2 = [1.99, 1.99, 0.99, 1.99, 0.99, 1.99, 0.99, 0.99]
a3 = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
a4 = [10.01, -12.22, 0.23, 19.20, -5.13, 3.12]

#UCID-rk268 Date-2/5/2023
def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    total = 0.00
    #TODO add necessary code here for sum; every number must have two decimal places shown
    #print("\nThe total is {}:\n".format(total))
    for i in range(0,len(arr)):
        total = total + arr[i]
    print("\nThe total is {:.2f}:\n".format(total))
    #print("\nThe total is {}:\n".format(total))


print("Problem 2")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
