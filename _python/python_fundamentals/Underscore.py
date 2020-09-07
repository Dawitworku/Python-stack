class Underscore:


    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])   #passing on the data/index values for the callback(lambda)
        return iterable   # returning the list

    def find(self, iterable, callback):
        for i in iterable:
            if callback(i):
                return i

    def filter(self, iterable, callback):  # The lambda function return a boolean. To go around it and print the array/list, we can create a new list, add the True values to the new array and print the new array.
        new_list = []

        for i in iterable:
            if callback(i):           # if list values are divisible by 2:
                new_list.append(i) 
        return new_list

    def reject(self, iterable, callback):
        new_list = []

        for i in iterable:
            if not callback(i):
                new_list.append(i)
        return new_list


underscore = Underscore() # yes we are setting our instance to a variable underscore. Creating an object of the class
# calling our map function here!
w = underscore.map([1,2,3,4,5,6,7,8,9,10], lambda x: x*2)
print(w)
# calling our find function here!
x = underscore.find([1,2,3,4,5,6], lambda x: x>4)
print(x)
# calling our filter function here!
y = underscore.filter([1,2,3,4,5,6], lambda x: x%2==0)
print(y)
z = underscore.reject([1,2,3,4,5,6], lambda x: x%2==0)
print(z)