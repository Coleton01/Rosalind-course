import re
from typing import Type, List


# noinspection PyTypeChecker
def loopSum():
    file_path = r'C:\Users\coled\PycharmProjects\pythonProject3\Rosalind\datasets\rosalind_ini4.txt'

    try:
        with open(file_path, 'r') as text_file:

            lines = text_file.readlines()
            lines = lines[0].strip()
            integers = re.findall(r'\d+', lines)
            integers = [num for num in integers if num.strip()]
            integers = [int(num) for num in integers]
            print(integers)
            print("_____________________")
            # variables
            start = integers[0]
            end = integers[1]
            if start > end:  # ensure start <= end
                start, end = end, start  # tuple unpacking, a tuple is an ordered collection of elements, enclosed
                # in parentheses (), (element1,element2, etc)    (start,end) = (end,start)
            total = 0

            for num in range(start, end + 1):  # sort for odd and summation
                if num % 2 != 0:
                    total += num

            print(total)



    except FileNotFoundError:
        print("File not found at the specified path.")
    except IOError:
        print("An error occurred while reading the file.")
    except Exception as e:
        print("An error occurred:", str(e))


loopSum()
