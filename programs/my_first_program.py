from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    
    # Inputs from Party1: a list of integers to be sorted
    input_list = [SecretInteger(Input(name=f"input_{i}", party=party1)) for i in range(10)]
    
    def counting_sort(arr, exp):
        n = len(arr)
        
        # The output array elements that will have sorted arr
        output = [SecretInteger(0) for _ in range(n)]
        
        # Initialize count array as 0
        count = [SecretInteger(0) for _ in range(10)]
        
        # Store count of occurrences in count[]
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
        
        # Change count[i] so that count[i] now contains the actual
        # position of this digit in output[]
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        # Build the output array
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        
        # Copy the output array to arr[], so that arr now
        # contains sorted numbers according to current digit
        for i in range(n):
            arr[i] = output[i]
    
    def radix_sort(arr):
        # Find the maximum number to know the number of digits
        max_val = arr[0]
        for num in arr:
            if num > max_val:
                max_val = num
        
        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is the current digit number
        exp = 1
        while max_val // exp > 0:
            counting_sort(arr, exp)
            exp *= 10
    
    # Perform radix sort on the input list
    radix_sort(input_list)
    
    # Output the sorted list
    sorted_outputs = [Output(input_list[i], f"sorted_output_{i}", party1) for i in range(10)]
    
    return sorted_outputs

