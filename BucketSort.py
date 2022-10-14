from math import floor
def bucket_sort(input):
    normalized = normalize(input)
    return bucketize(input,normalized)
    
def bucketize(input,normalized):
    n = len(input)
    bucket_list = [[] for i in input]
    for i in range(n):
        index = floor(normalized[i]*n)
        bucket_list[index].append(input[i])
    #Create sorted after merging
    sorted_array =[]
    for bucket in bucket_list:
        sorted_array += sorted(bucket)
    return sorted_array

def normalize(input):
    min_val=min(input)
    max_val = max(input)
    return [(x-min_val)/(max_val-min_val+(1/len(input)**2)) for x in input]
    
input = [3,6,2,8,7,9,5,1,4]
print(bucket_sort(input))
