def process_file(input_file_path, output_file_path):
    unique_integers = {}

<<<<<<< HEAD
    
    with open(input_file_path, 'r') as input_file:
        
=======
    with open(input_file_path, 'r') as input_file:
    
>>>>>>> 2507e8e7b68d606664ea41fb55245a274c65c707
        for line in input_file:
            try:
                
                number = int(line.strip())
<<<<<<< HEAD
                
                if -1023 <= number <= 1023:
                    
                    unique_integers[number] = True
            except ValueError:
                
                pass

    
    sorted_integers = list(unique_integers.keys())

    
    def bubble_sort(arr):
        n = len(arr)

        for i in range(n):
            
            for j in range(0, n - i - 1):
        
                
=======
            
                if -1023 <= number <= 1023:
                
                    unique_integers[number] = True
            except ValueError:
            
                pass

    sorted_integers = list(unique_integers.keys())

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
        
            for j in range(0, n - i - 1):
                # Traverse the array from 0 to n-i-1
            
>>>>>>> 2507e8e7b68d606664ea41fb55245a274c65c707
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

<<<<<<< HEAD

    sorted_integers = bubble_sort(sorted_integers)
    print(sorted_integers)


=======
    sorted_integers = bubble_sort(sorted_integers)
    print(sorted_integers)

>>>>>>> 2507e8e7b68d606664ea41fb55245a274c65c707
    with open(output_file_path, 'w') as output_file:
        for number in sorted_integers:
            output_file.write(str(number) + '\n')

<<<<<<< HEAD

    print("integers to my", output_file_path)
=======
    print("Unique integers written to", output_file_path)
>>>>>>> 2507e8e7b68d606664ea41fb55245a274c65c707

process_file("results_for_sample_inputs/sample_01.txt_result.txt", "sample_input_for_students/sample_01.txt")
