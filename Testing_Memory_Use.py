import pickle
import random
import sys


# Testing the size of Data

test_dict = {}
medium_test = {}
larger_test = {}

four_mb_max = {}

while sys.getsizeof(four_mb_max) < 4000000:
    x = random.randint(0, 1000000)
    four_mb_max[x] = (x, x)

print(len(four_mb_max))

# for x in range(3150):
#     a = random.randint(0, 10201)
#     b = random.randint(0, 10201)
#     test_dict[x] = (a, b)
#
# with open("test_dictionary", "wb") as handle:
#     pickle._dump(test_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
# for x in range(0, 302600):
#     a = random.randint(0, 1002001)
#     b = random.randint(0, 1002001)
#     larger_test[x] = (a, b)
#
# with open("larger_dictionary", "wb") as handle:
#     pickle._dump(larger_test, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
# for x in range(0, 248500):
#     a = random.randint(0, 826281)
#     b = random.randint(0, 826281)
#     medium_test[x] = (a, b)
#
# with open("medium_dictionary", "wb") as handle:
#     pickle._dump(medium_test, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
# print(sys.getsizeof(test_dict))
# print(sys.getsizeof(larger_test))
# print(sys.getsizeof(medium_test))


# pickle must be using compression because the saved file size is much smaller than what sizeof returns
