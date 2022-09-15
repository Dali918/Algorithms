def insertionSort(nums):
    for j in range(1,len(nums)):
        i = j-1                     # start at index before j
        key = nums[j]               # find the key 
        while i>-1 and nums[i]>key: #find index to insert   
            nums[i+1] = nums[i]     # shift elements
            i-=1                    
        nums[i+1] = key             #insert at appropriate index
    return nums

def test(test_bench):
    for test in test_bench:
        print(f"{sorted(test)} = {insertionSort(test)}")
        assert(sorted(test)==insertionSort(test))
    print("Tests passed")
test_bench =[[5,1,2,38,9],[1],[1,2,3],[6,9,8,7,5]]
test(test_bench)
        
