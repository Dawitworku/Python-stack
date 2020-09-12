Assignment: Intro to TDD
Objectives:
Practice writing and running tests on an algorithm


reverseList - Write a function that reverses the values in the list (without creating a temporary array).
Example: reverseList([1,3,5]) should return [5,3,1]
Example Test: assertEqual( reverseList([1,3,5]), [5,3,1] )
Add at least 3 other test cases
isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).
Example: isPalindrome("racecar") should return True
Example Test: assertEqual( isPalindrome("racecar"), True ) or assertTrue( isPalindrome("racecar"))
Example Test: assertFalse( isPalindrome("rabcr") ).
Add at least 5 other test cases
coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.
Example: given 87 cents, result should be 3 quarters, 1 dime, 0 nickel and 2 pennies
Example Test: assertEqual( coin(87), [3,1,0,2] )
Add at least 5 other test cases
BONUS - factorial - Write a recursive function that returns the factorial of a given number. Remember that the factorial of a number is the product of all the numbers between 1 and the given number (eg. 4! = 4*3*2*1).
Example: factorial(5) should return 120.
Add at least 3 test cases
BONUS - fibonacci - Write a recursive function that accepts a number, n, and returns the nth Fibonacci number from the sequence. The first two Fibonacci numbers are 0 and 1. Every number after that is calculated by adding the previous 2 numbers from the sequence. (i.e. 0, 1, 1, 2, 3, 5, 8, 13, 21 ...)
Example: fibonacci(5) should return 3 (the 5th number in the sequence is 3).
Add at least 3 test cases