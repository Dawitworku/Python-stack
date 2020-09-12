import unittest

def reverseList(arr): #a,b = b,a
    for i in range(int(len(arr) / 2)):
        arr[0 + i], arr[len(arr)-1 -i] = arr[len(arr)-1 -i], arr[0 + i]
    return arr

def isPalindrome(word):
    reverse_word = reversed(word)
    if reverse_word == word:
        return True
    else:
        return False

def coin(num):
    coinChange = []
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    for i in range(num):
        if num > 25:
            num -= 25
            quarters += 1
        elif num > 10:
            num -= 10
            dimes += 1
        elif num > 5:
            num -= 5
            nickels += 1
        elif num >= 1:
            num -= 1
            pennies += 1
    coinChange.append(quarters)
    coinChange.append(dimes)
    coinChange.append(nickels)
    coinChange.append(pennies)
    return coinChange

class TestCase(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([1,2,3,4,5]), [5,4,3,2,1])
    def testTwo(self):
        self.assertEqual(reverseList([1,3,5]), [5,3,1] )
    def testThree(self):
        self.assertEqual(reverseList([10,20,30,40,50]), [50,40,30,20,10])
    def testFour(self):
        self.assertTrue(isPalindrome('racecar'))
    def testFour(self):
        self.assertFalse(isPalindrome('rabcr'))
    def testFive(self):
        self.assertEqual(coin(87), [3,1,0,2])
        
    def setUp(self):
        print('Running Setup')
    def tearDown(self):
        print('Running Teardown Tasks')

if __name__ == '__main__':
    unittest.main() # This will run our test
