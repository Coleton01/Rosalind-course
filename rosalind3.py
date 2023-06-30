# Rosalind problem 2 Given: a string s of length at most 200 letters and four integers a,b,c,d. return: the slice of
# this string from indices a through b and c through d (with space in between), inclusively. in other words,
# we should indclude leemetns s[b] and s[d] in our slice.
from typing import List
import re


def xfile():
    file_path = r'C:\Users\coled\PycharmProjects\pythonProject3\Rosalin\rosalind_ini3.txt'
    try:
        with open(file_path, 'r') as text_file:  ##open file
            lines = text_file.readlines()

            if len(lines) >= 2:                 ##if else for length check
                x = lines[0].strip()
                y = lines[1].strip()
                print('Contents of the file:')
                print(lines)
                print("x =", x)
                print(y)
                print("______________________________________________")

                integers = re.findall(r'\d+', y)
                integers = [num for num in integers if num.strip()]
                integers = [int(num) for num in integers]

                a = integers[0]
                b = integers[1]
                c = integers[2]
                d = integers[3]
                print("your text is:")
                print(x[a:b + 1], x[c:d + 1])  # add 1 to count for inclusivity
            else:
                print("File does not have enough lines.")
    except FileNotFoundError:
        print("File not found at the specified path.")
    except IOError:
        print("An error occurred while reading the file.")
    except Exception as e:
        print("An error occurred:", str(e))


xfile()
