egg_count = 0

def buy_eggs(count):
    return count +12 # purchase a dozen eggs
egg_count=buy_eggs(egg_count)

numbers=[
         [34,63,88,71,29],
         [90,78,51,27,45],
         [63,37,85,46,22],
         [51,22,34,11,18],
]
averages=list(map(lambda x:sum(x)/len(x),numbers))
print(averages)

cities=["NewYork City","Los Angels","Chicago","MountainView","Denver","Boston"]
short_cities=list(filter(lambda x:len(x)<10,cities))
print(short_cities)

for x in range (+100):
    print(x)

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))

sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares