########################################################################################################################
# Class: Computer Networks
# Date: 08/30/2021
# Lab0: Getting Started with Python
# Goal: Learning the basics of Python
# Student Name: Jonathan McGrath
# Student ID: 918145233
# Student Github Username: JonOct45
# Instructions: Complete the TODO sections for each problem
# Guidelines: Read each problem carefully, and implement them correctly. Grade is based on lab correctness/completeness
#               No partial credit will be given.
#               No unit test are provided for lab #0
########################################################################################################################

########################## Problem 0: Print  ###########################################################################
"""
Print your name, student id and Github username
Sample output:
Name: Jose
SID: 91744100
Github Username:
"""
import unittest

name = "Jonathan"  # TODO: your name
SID = 918145233 # TODO: your student id
git_username = "JonOct45"  # TODO: your github username
print(name)
print(SID)
print(git_username)
print('\n')

########################## Problem 1: product or sum ############################################################
"""
Given two values representing two integers, return their product if it is less or equal than the threshold, 
Otherwise, return their sum. 
Example with product: value1 = 2, value2 = 3, threshold = 100 will return 6
Example with sum: value1 = 2, value2 = 100, threshold = 100 will return 102
"""


def product_or_sum(value1, value2, threshold=100):
    """
    :value1: an integer representing the first value
    :value2: an integer representing the second value
    :threshold: an integer representing the limit for the product of the two values
    :return: the product or the sum of both values
    """
    result = 0
    # TODO: your code here

    total = value1 * value2

    if total >= threshold:
        result = value1 + value2
    else:
        result = value1 * value2

    return result


########################## Problem 2: String Processing ##############################################################
"""
Given a string print the number of times the another string appears anywhere in the given string

For example, given the string: "Alice and Bob go to the same school. They learned today in class how to treat a lice 
infestation, and Alice found the lecture really interesting". the string "Alice" will be found 2 times. 
"""


def str_times_found(str_to_find, original_str):
    """
    :str_to_find: the string to be found
    :original_str: the string where str_to_find may be found.
    :return: an integer representing the number of times str_to_find was found
    """

    # TODO: your code here

    result = original_str.count(str_to_find)

    return result

#Assigning the result to a variable, 
#resulted = str_times_found(strtofind,stringed)

#Printing the result count of the string
#print(resulted)



########################## Problem 3: Loops ############################################################################
"""
Given a list of numbers iterate over them and output the sum of the current number and previous one.

Given: [5, 10, 24, 32, 88, 90, 100], returns [5, 15, 34, 56, 120, 178, 190]
"""


def summation(list_of_integers):
    """
    :list_of_integers: represents the given list of integers
    :returns: a new list where the value in index (i) is the sum of list_of_integers[i-1] + list_of_integers[i]
    """
    result = []
    # TODO: your code here

    #Index counter
    index = 0

    #For loop iterating through the list_of_integers list
    for x in list_of_integers:
        
        #If it is the first item in the list, skipping
        if list_of_integers[index]== list_of_integers[0]:
            result.append(list_of_integers[0])

            #Incrementing the index counter
            index+=1
        else:
            #Appending the result to the list Result
             result.append(list_of_integers[index] + list_of_integers[index-1])
            
            #Incrementing the index counter
             index += 1
             

    return result


########################## Problem 4: Merging Lists ##########################################################
"""
Given two unordered lists as parameters, return a new list with all the 
odd numbers from the first and second list sorted in ascending order. 

For example: Given l1 = [2,1,5,7,9] and l2 = [32,33,13] the function will return odds = [1,5,7,9,13,33] 
"""


def merge_odds(list1, list2):
    """
    :list1:
    :list2:
    :return: a new ordered list with all the odds values from both lists.
    """
    odds = []
    # TODO: your code here

    #Creating Temp list to store the lists
    temp_array = list1 + list2

    #Appending any odd numbers to the odd list
    for x in temp_array:
        if x %2 != 0:
            odds.append(x)
        
    #Sorting the odds in ascending order
    odds.sort()

    return odds


########################## Problem 5: Dictionaries ###################################################
"""
Refactor problem #4 to return a python dictionary instead of a list where the keys are the indexes of the odd numbers 
(from list1 and list2) and the values are the odd numbers. 

For example: Given [2,1,5,7,9] and [32,33,13] the function returns {1: [1, 33], 2: [5,13], 3: [7], 4: [9]} 
"""


def merge_odds_with_keys(list1, list2):
    """
    :list1:
    :list2:
    :return: a Python dictionary of keys (indexes in list1 and list2), and values are the odd values.
    """
    odds = {}
    # TODO: your code here

    len_list1 = len(list1)
    len_list2 = len(list2)
    longest_len = max(len_list1,len_list2)

    difference = abs(len_list1 - len_list2)

    if len_list1 > len_list2:
        list2.extend([2]*difference)
    elif len_list2 > len_list1:
        list1.extend([2]*difference)

    #Creating new list, zipping together the Range List / List1 and List2
    new_list = zip(list(range(longest_len)),list1,list2)

    #Iterating through each item in the new list, 
    for i, item1, item2 in new_list:
        odd_list = []
        if item1 % 2 != 0:
            odd_list.append(item1)
        if item2 % 2 != 0:
            odd_list.append(item2)
    #If the list has items, appending to the odds list        
        if len(odd_list) != 0:
            odds[i] = odd_list
    



    # print(longest_len)

    # for i in range(longest_len):
    #     odd_list = []
    #     if i < len_list1:
    #         if list1[i] % 2 != 0:
    #             odd_list.append(list1[i])
    #     if i < len_list2:
    #         if list2[i] % 2 != 0:
    #             odd_list.append(list2[i])
    #     if odd_list:
    #         odds[i] = odd_list


    
        
    return odds


######################## Unit Tests (Do not modify) ##################################################################

class TestCases(unittest.TestCase):
    def testP1(self):
        self.assertEqual(product_or_sum(2, 5), 10)
        self.assertNotEqual(product_or_sum(2, 5, threshold=9), 10)

    def testP2(self):
        str = "Alice and Bob go to the same school. They learned today in class how to treat a lice" \
              "infestation, and Alice found the lecture really interesting"
        self.assertEqual(str_times_found("Alice", str), 2)

    def testP3(self):
        list_of_values = [5, 10, 24, 32, 88, 90, 100]
        self.assertEqual(summation(list_of_values), [5, 15, 34, 56, 120, 178, 190])

    def testP4(self):
        list1 = [2, 1, 5, 7, 9]
        list2 = [32, 33, 13]
        odds = merge_odds(list1, list2)
        self.assertEqual(odds, [1, 5, 7, 9, 13, 33])

    def testP5(self):
        list1 = [2, 1, 5, 7, 9]
        list2 = [32, 33, 13]
        odds = merge_odds_with_keys(list1, list2)
        self.assertEqual(odds, {1: [1, 33], 2: [5, 13], 3: [7], 4: [9]})


if __name__ == '__main__':
    unittest.main()
