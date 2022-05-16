print("input data : data amount and target_data ex)10 7")
n, target = map(int,input().split())
print("input data : data list ex)1 2 3 4 ...")
array = list(map(int,input().split()))

def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

result = binary_search(array,target,0,n-1)
if result == None:
    print("No exist target_data")
else:
    print(result+1)

'''
input
10 7
1 3 5 7 9 11 13 15 17 19
output
4
'''