pos = -1

def search(list,n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u)//2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1
    return False

list=[1,2,3,4,5,6,7] # list must b e sorted
n = int(input('Please enter the number between 1 to 7: '))

if search(list,n):
    print(f'Found at {pos} index ')
else:
    print('Not Found')