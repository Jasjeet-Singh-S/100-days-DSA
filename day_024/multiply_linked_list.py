# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def multiply_two_lists(self, first, second):
        string_1 = ""
        string_2 = ""
        while first!=None:
            string_1 += str(first.data)
            first = first.next
        while second!=None:
            string_2 += str(second.data)
            second = second.next
        num_1 = int(string_1)
        num_2 = int(string_2)
        return (num_1*num_2)%((10**9) + 7)
    
# https://www.geeksforgeeks.org/multiply-two-numbers-represented-linked-lists/