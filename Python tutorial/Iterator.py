nums = [5, 5, 4, 87, 76, 67, 6879, 6, 56, 5, 64, 96]

it = iter(nums)
print(it.__next__())
print(it.__next__())
print(it.__next__())

for i in nums:
    print(i)


# Generator

def colourCodes():
    yield 'c1'
    yield 'c2'
    yield 'c3'
    yield 'c4'


cc = colourCodes()

print(cc.__next__())
print(cc.__next__())

for i in cc:
    print(i)


def topSqr():
    for i in range(1, 11):
        yield i * i


sq = topSqr()

for i in sq:
    print(i)

