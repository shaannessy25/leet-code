# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M
# Given a roman numeral, convert it to an integer. Input is guranteed to be within the range
# from 1 to 3999. 
#Symbol  Value
#I       1
#V       5
#X       10
#L       50
#C       100
#D       500
#M       1000

# Example 1: input = III => output = 3
# Example 2: input = IV => output = 4

# Restate the problem: 
# Create a function or class that takes in roman numerals as an input and
# converts the letters to it's corresponding number value and return the numerical value. The
# function also needs to recognize the roman numeral pattern i.e. IV not IIII.

# Clarifying questions:
# Where are the inputs coming from? Is it stored in memory or is it from the user? Will the output print or return?
# Will a print or return an integer or a string? 

# Stating Assumptions:
# Input is a string, output will be an integer. Input will be no greater than 3999. input will be given by the user.

# Brainstorm:
# Use a dictionary to store values of the roman numerals. Transverse through the list and replace numerals with integer value
# Add all the integers together then return the string

# Explaining rationale:
# Using a dictionary would be the fastest way to convert string to integer value. when we transverse through the list we can
# Find the corresponding value from the key and add the integers.

# Tradeoffs:

# Improvements:
# Needs to be able to take in lower case letters as valid inputs. Optimize the method to get higher values.



class Solution(object):

    def convert(self):
        roman = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'IL': 49, 'L':50, 'IC': 99, 'C':100, 'ID': 499, 'D':500,'IM': 999, 'M':1000 }
        i = 0
        num = 0
        while i < len(s):
            if i + 1 < len(s) and s[i: i + 2] in roman:
                num += roman[s[i: i + 2]]
                i += 2
            else:
                #print(i)
                num += roman[s[i]]
                i+=1
        return num



s = 'iii'

print(Solution.convert(s))