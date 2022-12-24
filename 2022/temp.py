#%%
def binary_search(arr: list[int], target: int):
	start = 0
	end = len(arr) - 1
	mid = 0	
	while start <= end:
		
		mid = start + (end - start)//2
		
		if arr[mid] == target:
			return mid
		
		if arr[mid] < target:
			start = mid + 1
		
		if arr[mid] > target:
			end = mid - 1
		
	return -1


# %%
def eval(func, test_cases: list[dict]):
    for ind, test_case in enumerate(test_cases):
        input = test_case["input"]
        target = test_case["target"]
        output = test_case["output"]
        op = func(input, target)
        if op == output:
            print(f"Test {ind+1} passed")
        else:
            print(f"Test {ind+1} failed")


# %%
test_cases = [
    {
        "input": [1,2,3,4,5,6],
        "target": 3,
        "output": 2
    },
    {
        "input": [],
        "target": 3,
        "output": -1
    },
    {
        "input": [1],
        "target": 1,
        "output": 0
    }
]
eval(binary_search, test_cases)


# %%

def num_rotated(arr: list[int]):
	N = len(arr)
	start = 0
	end = N - 1
	mid = 0
	while start <= end:
		mid = start + (end-start)//2
		
		next = (mid + 1) % N
		prev = (N + mid - 1) % N   # Not sure if this N + is needed
		
		if arr[prev] > arr[mid] and arr[mid] < arr[next]:
			return mid     # or N-mid if rotated left
		
		if arr[start] <= arr[mid]:
			start =  mid + 1

		if arr[mid] <= arr[end]:
			end = mid - 1


# %%
# 1,2,3
# 3,1,2
# 2,3,1
arr = [2, 2, 3, 1]
num_rotated(arr)




# %%
