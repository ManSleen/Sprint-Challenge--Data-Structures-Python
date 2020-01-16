from binary_search_tree import BinarySearchTree
import time
import sys
sys.path.append('../binary_search_tree')

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
bst1 = BinarySearchTree("Michael VanSleen")

for name_1 in names_1:
    bst1.insert(name_1)

for name_2 in names_2:
    if bst1.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# I think the runtime complexity of the starter code was O(n^2) since we had a loop inside of another loop and we did not change the amount of data we were looping through, each element in the first loop required a loop through the second set of data, so O(n * n) which is O(n^2)
