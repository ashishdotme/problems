#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created by Ashish Patel
Copyright © 2017 ashish.me
ashishsushilpatel@gmail.com
"""

"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""

# Time:  O(n * k), k is the length of the common prefix
# Space: O(1)

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return "{} -> {}".format(self.val, self.next)
				
class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type s: str
		:rtype: bool
		"""
		l = ListNode(0)
		ret = l
		while l1 and l2:
			if l1.val <= l2.val:
				l.next, l1 = l1, l1.next
			else:
				l.next, l2 = l2, l2.next
			l = l.next
		l.next = l1 or l2
		return ret.next

if __name__ == "__main__":
		l1 = ListNode(0)
		l1.next = ListNode(1)
		l2 = ListNode (2)
		l2.next = ListNode(3)
		print(Solution().mergeTwoLists(l1, l2))
