#Akinola Daramola Jr
#Programming Exercise: 6.9
#Due Date: 07.27/2022


"""
Exception Handing
Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
It should handle any IOError exceptions that are raised when the file is opened and data is read from it.
It should handle any ValueError exceptions that are raised when the items that are read from the file are converted to a number.

"""

#Declaring mainline function
def main():
    #Implementing try/except block for errors
    try:
        #Creating object of file 'numbers.txt'
        numbers_file = open('numbers.txt', 'r')

        #Initializing variables 'average', 'total' and 'number_of_lines'
        average = 0
        total = 0
        number_of_lines = 0

        #Constructing a for loop to iterate through object
        for digits in numbers_file:
        
            #Adding the sum of all digits in object file 'number.txt'    
            total += int(digits)

            #number_of_line value increases 1 unit every iteration until loop ends
            number_of_lines += 1
            #print(number_of_lines)
        
            
        #Calculating the average by dividing total by number of lines in file  
        average = total / number_of_lines

        #Displaying average of sum of digits added
        print(f"Average: {average:.2f}")


        #Closing numbers file
        numbers_file.close()

    except IOError:
        print(f"Error: File name not found");

    except ValueError:
        print('Error: Please enter a number.')
        

#Calling mainline function
main()
