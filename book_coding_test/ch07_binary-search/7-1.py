def sequentialSearch(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1
n = 5
target = "Dongbin"
array = ["Hanul", "Jonggu", "Dongbin", "Taeil", "Sangwook"]
print(sequentialSearch(n, target, array))
