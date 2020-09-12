import unittest

class MathDojo:

    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        splat = 0
        for i in nums:
            splat += i
        self.result += num + splat
        return self
    
    def subtract(self, num, *nums):
        splatvar = 0
        for i in nums:
            splatvar -= i
        self.result -= (num - splatvar)
        return self

md = MathDojo()


class TestCase(unittest.TestCase):
    def setUp(self):
        md = MathDojo()
        print('Running Setup')

    def test_one(self):
        self.assertEqual(md.add(2,3).result, 5)
    def test_two(self):
        self.assertEqual(md.subtract(15,5,5).result, -20)


    def tearDown(self):
        print('Running Teardown Tasks')

if __name__ == '__main__':
    unittest.main() # This will run our test

