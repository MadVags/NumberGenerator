import random

class RandomNum():

    def __init__(self, range_start, range_end, num_items):
        self._range_start = range_start
        self._range_end = range_end
        self._num_items = num_items
        self.count = 0

    def __RandNum__(self):
        if self.count < self._num_items:
            self.count += 1
            return random.randint(self._range_start, self._range_end)


start = input("Starting Number: ")
end = input("Ending Number: ")
num = input("Amount of Numbers: ")


x = RandomNum(int(start), int(end), int(num))

for _ in range(int(num)):
    try:
        print(x.__RandNum__())
    except:
        print("Done")

