input = [3,6,2,8,7,9,5,1,0]
print(len(input))

def swap(array,i,j):
    
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    

def partition(input,l,h):
    pivot_val = input[h]
    new_pivot = l
    for j in range(l,h):
        if input[j]<=pivot_val:
            swap(input,new_pivot,j)
            new_pivot+=1
            # print(f"value of left_wall {left_wall}")
    swap(input,new_pivot,h)
    return new_pivot
def quick_sort(input,l,h):
    if l >= h:
        return
    print(input)
    pivot = partition(input,l,h)
    print(pivot,l,h)
    quick_sort(input,l,pivot-1)
    quick_sort(input,pivot+1,h)
    
    
quick_sort(input,0,len(input)-1)    
print(input)

        
    
