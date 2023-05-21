[toc]

# Easy

## 1. Two Sum [2023-03-22] py
```
brute force search 
	silly O(n^2)

binary search 
	O(n log n) better
	***not best solution, wasted some time implementing here***

dict search
	think about time complexities
		biggest issue is search time
		reference big O cheat sheet
	O(1) search in hash table desirable
		O(n) to populate hash table
		O(n) is probs best we'll get
```

### dict/hm search
O(n) = O(n) + O(n)
```
iterate list
	fill dict[k=n, v=[i0,i1,...]]
iterate list
	find indexes using dict
```
### binary search
O(n log n) = O(n) * O(log n)
```
iterate list
	binary search target
```
### brute force search
O(n^2) = O(n) * O(n)
```
iterate list
	built in search target
```

## 9. Palindrome Number [2023-03-23] py
```
str conversion
	straightforward solution
no str conversion 
	comparison with just one int weird
	two ints easier to work with
	how do we chop and grab right digit? biggest issue
```

### convert to str, brute compare
O(n)
```
convert to string
iterate low, high pairs
	compare low high
```

### no str conv., reverse int buildup, then direct compare
O(n)
```
deal with special cases, n >= 1 always after
	false if negative, positive 0 in ones digit
	positive if 0
iterate by digit amount 
	keep chopping off right last digit
		math.floor(20302 * .10)
	add right digit to reverse
```

## 13. Roman to Integer [2023-03-24] java
```
cursor 
	seemed more annoying than other solution
	have to worry about placement of cursor
```
### numeral reader machine
O(n)
```
looping, destructive, feed s into a machine
1) empty string
	stop
2) single length string
	sum += single numeral
	stop
3) 2+ length string
	sum += single numeral
	chop single left letter
	OR
	sum += double numeral
	chop double left letters
```

### cursor
O(n)
```
incrementing cursor
	+1 for single numeral, +2 for double numeral
```

# 14. Longest Common Prefix [2023-03-26] py
```
brute compare
	use built python built in functions
	make writing code faster
	we cannot avoid O(n^2) in any solutions I think

hashmap smarter brute
	seems complicated
	doesn't help with complexity in some cases
	weird
```

### brute compare
O(n^2)
```
pick largest word as compare word
prefix = '' to start

iterate other words
	iterate all prefix poss of compare word
		if not match return prefix
```

### hashmap smarter brute
???
```
hashmap
	4: 'flow', 'flew'
	6: 'flower', 'flight'
go level by level
advantages:
	one nonmatching small word, faster
```

## 20. Valid Parentheses [2023-03-27] py
```
time complexity is not an issue
always O(n)

stack compare
	determine valid parenthesis is basically a stack
	use list as stack structure, hold left symbols
	three cases when false
		1) mismatch
		2) not enough left
		3) too many left
	otherwise true
```

O(n)
### stack compare
iterate ch in s
	if left symbol
		append to left stack
	else right symbol
		pop left stack and compare

## 21. Merge Two Sorted Lists [2023-03-28] py
```
kinda straightforward
having a advance method as helper is useful
```

### idk name solution
```
list1 list2 pointers -> compare, and advance
list3
	curr pointer 
	head pointer

loop until list1 list2 are None
	both list1 and list2 have value
		list1 value less than list2
			advance
		list2 value less than list1
			advance
	only list2 has value
		advance
	only list1 has value
		advance

define advance function
advance takes curr and either list1 or list2
	extend the return linkedlist
	advance either list1/list2 pointers
```

## 26. Remove Duplicates from Sorted Array [2023-03-28] py
```
py solutions
	list data type is mutable
	mutable args in methods get reference to same object
	rebinding nums within function means original ref outer nums is cut off now
	so do not rebind, edit in place, no cutting off reference
```

### clear, then extend
O(n)
```
init duplicate stack with first num
iterate over nums, except 1st elem
	if not duplicate, append to stack
clear nums
extend nums with stack list
return length
```

### built in sort()
O(n log n)
```
list as stack to store unique numbers
iterate elements in nums
	add to stack if unique
	else set new list value to value over max constraint
in place sort the list
```

### in place removal
O(n^2)
```
stack1 = unique numbers

iterate over nums
	if duplicate remove
	else append to stack1
```

## 28. Find the Index of the First Occurrence in a String [2023-03-28] py 
```
weird idea with double cursor
idk what i was thinking
helped get to better slicing idea
```

### slice hay, compare needle
O(n)
```
slice haystack into needle sizes
	take slice and compare to needle
```

### double cursor
```
messes up on sasadsa, sad
from this idea -> better solutino

two cursors
	haystack cursor
		continually advance
	needle cursor
		if needle letter == haystack letter
			advance
		else not match
			reset needle
```

### built in find()
O(n)
```
just use built in method
this feels like "cheating" tho
```

## 66. Plus One [2023-03-29] py
```
three examples
	[9, 9, 9]
	[1, 9, 9]
	[1, 2, 3]
```

### no conversion, in place
O(n)
```
add 1 to digit
	sum 10
		next exists -> sum 10 loop
		no next -> add lead zero
	sum 1-9, we end
```

### str conversion
???
```
iterate digit in digits list
	add to formed string
convert string to int, add 1, convert to str again
iterate characters
	add to new return list
return list
```

## 69. Sqrt(x) [2023-03-29] py
```
```

### binary search
O(log n)
```
should take 32 operations
log_2(2^32)


```

### brute force
O(n)
```
2^32 operations long, way too slow

iterate 0, 1, 2, ... 2^32
	power 2 each number
	if x equal
		return
	else x inbetween
		round down
```

## 70. Climbing Stairs
```
dunno why I had trouble with this one
distracted by b-tree solution
got lost in rabbit hole of b-tree and fib
```

### simple buildup
O(n)
```
store ways for one below and two below

build way up from bottom up

cs(4) = cs(3) + cs(2)
cs(3) = cs(2) + cs(1)
cs(2) = 2
cs(1) = 1
```

### fibonacci?
O(2^n)
```
basically a binary tree
just carbon copy fib code in here, it'll work slow
```

## 88. Merge Sorted Array [2023-04-02] py
```
couldn't figure out O(m + n)
what is with the obsession with in place sorts on leetcode???
contrived problem
```

### built in sort
O(n log n)
```
store copy of nums1 with zeros removed
clear nums1
merge copy and nums2 with cleared nums1
nums1.sort()
```

## 94. Binary Tree Inorder Traversal [2023-04-03] py
```
iterative is more confusing than recursive
can't wrap my head around it that well
```

### iterative
O(n)
```
curr represents root of subtree not visited

curr = root
list = []

if curr exists
	append to stack (we process in order)
	curr = curr.left
elif stack exists
	process the stack
		pop top of stack
		set curr to popped value
		append to list
	curr = curr.right
```

### recursive
O(n)
```
inorder(NODE, list)
	if NODE None stop
	inorder(left, list)
	print/store NODE
	inorder(right, list)
```

## 412. Fizz Buzz [2023-04-20] java js py
```
basic problem
try languages
```

## 101. Symmetric Tree [2023-05-21] py
```
refer to 94. Binary Tree Inorder Traversal
pair off nodes, all nodes should have property below:
	sym(l, r) to sym(r, l)
symmetry defined as
	symmetric if both null
	nonsymmetric is one null
	symmetric if values match
```

##

# Medium

# Hard