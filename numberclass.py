import random

class MyIterator():

    def __init__(self, range_, num_items):
        self._range = range_
        self._items = num_items
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self._items:
            self.count+=1
            return random.randint(0, self._range)

        else:
            raise StopIteration




i1 = MyIterator(10, 10)

for _ in range(11): # will error on 6th iteration
    try:
        print(i1.__next__())
    except:
        print('No more elements.')
