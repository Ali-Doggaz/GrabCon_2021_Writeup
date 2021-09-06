import copy
# Python3 implementation of the
# above approach
list_numb = [271411, 1172549, 5535180, 4940226, 7280926, 5026654, 2472985] #n
sums_dict = dict()
all_binary_comb = []
# Function to print the output
def printTheArray(arr):
    sum = 0
    for i in range(0, 7):
        if arr[i]:
            sum= sum + list_numb[i]

    if sum in sums_dict:
        print("we have another combination for " + sum + ". It's " + arr)
    else:
        sums_dict[sum] = copy.deepcopy(arr);
    

 
# Function to generate all binary strings
def generateAllBinaryStrings(n, arr, i):
 
    if i == n:
        printTheArray(arr)
        return
     
    # First assign "0" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)
 
    # And then assign "1" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)
 
# Driver Code
if __name__ == "__main__":
 
    n = 7
    arr = [None] * n
 
    # Print all binary strings
    generateAllBinaryStrings(n, arr, 0)
    
    print(sums_dict)