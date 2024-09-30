import random
import time

steps = 0
swaps = 0

def inputArr():
    input_or_generate = input("Would you like to randomly generate a list (r), or input the values of one? (i): ")
    
    if input_or_generate == "r":
        while True:
            try:
                quantity = int(input("How many values in the array?: "))
                data_range = int(input("What is the range of the array?: "))
                if data_range < 1:
                    print("Range cannot be less than 1.")
                    continue
                break
                
            except ValueError:
                print("Invalid input.")
                continue
            
        return [random.randint(0, data_range) for i in range(quantity)]
    elif input_or_generate == "i":
        # .split() method

        while True:
            try:
                listArr = input("Enter the list in this format -> 104 593 305 >")
                data = listArr.split()
                for i in range(len(data)):
                    data[i] = int(data[i])
                break
            except ValueError:
                print("Invalid.")
                continue

        # individual values method
        
        """
        while True:
            try:
                quantity = int(input("How many values in the list?: "))
                break
            except ValueError:
                print("This is not a valid integer.")
                continue
            
        data = []
        for i in range(1, quantity+1):
            while True:
                try:
                    value = int(input("Enter value " + str(i) + ": "))
                    data.append(value)
                    break
                except ValueError:
                    print("This is not a valid integer.")
                    continue
        """
        
        return data

    else:
        print("Invalid.")
        return inputArr()

def partition(data, show_steps): # This is part of quicksort
    global steps
    global swaps
    idx_pointer = -1
    pvt_pointer = -1
    pvt = data[-1]
    for item in range(0, len(data)):
        idx_pointer += 1
        steps += 1
        if data[idx_pointer] <= pvt:
            pvt_pointer += 1
            if idx_pointer > pvt_pointer:
                data[pvt_pointer], data[idx_pointer] = data[idx_pointer], data[pvt_pointer]
                swaps += 1
                steps += 1
                if show_steps:
                    print("Two values swapped!")
                    print(data)
        else:
            pass
    return [data[0:pvt_pointer], data[pvt_pointer], data[pvt_pointer+1:]]

def quicksort(data, show_steps):
    
    total = partition(data, show_steps)
    
    if show_steps:
            print("Quicksorting left")
            
    if len(total[0]) > 1:
        left = quicksort(total[0], show_steps)
    else:
        left = total[0]

    if show_steps:
        print(left)
    
    
    if show_steps:
        print("Quicksorting right")
        
    if len(total[2]) > 1:
        right = quicksort(total[2], show_steps)
    else:
        right = total[2]
        
    if show_steps:
        print(right)
    
    
    return left+[total[1]]+right

def bubblesort(data, show_steps):
    global steps
    global swaps
    for h in range(len(data)-1):
        for i in range((len(data)-1)-h):
            steps += 1
            if data[i] > data[i + 1]:
                data[i], data[i+1] = data[i+1], data[i]
                steps += 1
                swaps += 1
                if show_steps:
                    print(data)
    return data

def selectionsort(data, show_steps):
    global steps
    global swaps
    for i in range(len(data)):
        for j in range(i, len(data)):
            steps += 1
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                steps += 1
                swaps += 1
                if show_steps:
                    print(data)
    return data

def pigeonholesort(data, show_steps):
    global steps
    min = data[0]
    max = data[0]
    for i in data:
        steps += 1
        if i < min:
            min = i
        if i > max:
            max = i
    size = max - min + 1
    pigeonholes = [0] * size
    print("Max:", max, "Min:", min)
    
    # Use a for loop through the list and put each item in a pigeonhole
    for i in data:
        steps += 1
        pigeonholes[i-min] += 1
        
    if show_steps:
        print("Pigeonholes:", pigeonholes)
    
    # Create a new list with the sorted data
    ans = []
    for i in range(len(pigeonholes)):
        steps += 1
        ans += [i + min] * pigeonholes[i]
        
        if show_steps:
            print(ans)
    return ans
    

def cocktailsort(data, show_steps):
    global steps
    global swaps
    for i in range(len(data)//2):
        for j in range(i, len(data)):
            steps += 1
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                steps += 1
                swaps += 1
                if show_steps:
                    print(data)
        for k in range(len(data)-1, i, -1):
            steps += 1
            if data[k] < data[k-1]:
                data[k], data[k-1] = data[k-1], data[k]
                steps += 1
                swaps += 1
                if show_steps:
                    print(data)
    return data

def main():
    global steps
    global swaps
    steps = 0
    swaps = 0
    data_set = inputArr() # input or generate
    
    if input("Do you want to print the shuffled list? (y/n): ") == "y":
        print(data_set)
    
    if input("Do you want to show the steps of the algorithm as it runs? (y/n): ") == "y":
        show_steps = True
    else:
        show_steps = False
        
    valid = False
    
    while not valid:
    
        sorting_type = input("Would you like to use:\nQuicksort (q),\nBubblesort (b),\nSelection sort (s),\nCocktail sort (c),\nor pigeonhole sort (p)?: ")
        
        if sorting_type == "q":
            valid = True
            t1 = time.time()
            data_set = quicksort(data_set, show_steps)
            timer = time.time() - t1
        elif sorting_type == "b":
            valid = True
            t1 = time.time()
            data_set = bubblesort(data_set, show_steps)
            timer = time.time() - t1
        elif sorting_type == "s":
            valid = True
            t1 = time.time()
            data_set = selectionsort(data_set, show_steps)
            timer = time.time() - t1
        elif sorting_type == "p":
            valid = True
            t1 = time.time()
            data_set = pigeonholesort(data_set, show_steps)
            timer = time.time() - t1
        elif sorting_type == "c":
            valid = True
            t1 = time.time()
            data_set = cocktailsort(data_set, show_steps)
            timer = time.time() - t1
        else:
            print("Invalid option.")
            
    print("Data sorted in %s milliseconds." % round(timer * 1000, 3))
    if sorting_type == "p":
        print("The number of steps is incremented each time through a loop iteration,\nincluding when finding the max and min values.")
        print("Number of steps:", steps)
    else:
        print("The number of swaps is incremented by 1 every time the algorithm swaps two values in the list.")
        print("The number of steps is incremented by 1 every time it checks values, \ndoes a loop iteration, or swaps two values in a list.")
        print("Number of swaps:", swaps)
        print("Number of steps:", steps)
    output_data_confirm = input("Would you like to print the sorted data set? (y/n): ")
    if output_data_confirm == "y":
        print(data_set)
        


while True:
    main()
    if input("Want to do another one? (y/n): ") == "n":
        break




