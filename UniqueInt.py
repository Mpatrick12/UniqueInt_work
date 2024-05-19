def process_file(input_file_path, output_file_path):
    unique_integers = {}

    # Open input file for reading
    with open(input_file_path, 'r') as input_file:
        # Iterate through each line in the input file
        for line in input_file:
            try:
                # Convert line to integer
                number = int(line.strip())
                # Check if the number falls within the range (-1023 to 1023)
                if -1023 <= number <= 1023:
                    # Add unique integers to the dictionary
                    unique_integers[number] = True
            except ValueError:
                # Skip non-integer lines
                pass

    # Convert dictionary keys to a sorted list
    sorted_integers = list(unique_integers.keys())

    # Bubble sort function to sort the list of integers
    def bubble_sort(arr):
        n = len(arr)
        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    # Sort the list of integers using the bubble sort function
    sorted_integers = bubble_sort(sorted_integers)
    print(sorted_integers)

    # Write sorted integers to the output file
    with open(output_file_path, 'w') as output_file:
        for number in sorted_integers:
            output_file.write(str(number) + '\n')

    # Print message indicating completion
    print("Unique integers written to", output_file_path)

process_file("results_for_sample_inputs/sample_01.txt_result.txt", "sample_input_for_students/sample_01.txt")
