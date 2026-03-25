# https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1

'''
    Your task is to delete the given node from
	the linked list, without using head pointer.
	
	Function Arguments: node (given node to be deleted) 
	Return Type: None, just delete the given node from the linked list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Solution:
    def deleteNode(self, del_node):
        # 1. Copy the value from the next node into the current node
        # (Using .val as is standard in LeetCode/ListNode definitions)
        del_node.data = del_node.next.data
        
        # 2. Skip the next node entirely
        # This is the "delete" step: the current node now points
        # to the one AFTER the next one.
        del_node.next = del_node.next.next