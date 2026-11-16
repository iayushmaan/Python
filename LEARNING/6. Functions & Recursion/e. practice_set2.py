# QUE 1
def sum(n):
    if n == 0:
        return 0
    return sum(n-1) + n

print(sum(8))





# QUE 2 
list = ["table", "chair", "watter bottle", "macbook", "airpods"]
def print_list(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx+1)

print_list(list)