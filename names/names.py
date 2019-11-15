import time
import sys
sys.path.append('../binary_search_tree')
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
bst1 = BinarySearchTree("Michael VanSleen")
bst2 = BinarySearchTree("Joseph Rios")

for name_1 in names_1:
    bst1.insert(name_1)

for name_2 in names_2:
    if bst1.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
