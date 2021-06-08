
# Array arr
print("Array arr")
arr = [10,20,30,"ultimo"]

print(arr)
print(arr[0])
print(arr[-1])

print(len(arr))
del arr[-1]
print(arr)
arr.remove(20)
print(arr)
arr.pop()
print(arr)
arr.insert(0, "uno")
print(arr)
arr.pop(1)
print(arr)

# Array concat
print ("Array concat")
concat = [1,2,3]
concat = concat + [4,5,6]
print(concat)

# Array repeat
print("Array repeat")
repeat = ["a"]
repeat = repeat * 3
print(repeat)

# Array slice
print("Array slice")
slice = ["uno", 2, 3, 4, "cinque"]
print(slice[2:])
