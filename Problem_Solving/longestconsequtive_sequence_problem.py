#longest consecutive sequence array = [100,4,200,1,3,2] o/p should be = 4

array = [100,4,200,1,3,2]

first solution 
sorted_array = sorted(array)
longest_sequence = 1

for ele in sorted_array:
    current_sequence = 1

    for j in range(len(sorted_array)):

        if ele+1 == sorted_array[j]:
            ele = ele + 1
            current_sequence = current_sequence + 1

    if current_sequence > longest_sequence:
        longest_sequence = current_sequence
        
print(longest_sequence)


# second solution 



nums = []
elements = set(nums)

max_seq = 0
seq_ele = []


for i in elements:
    current_seq = 1
    current_seq_ele = [i]

    if i-1 in elements :
        continue

    while i+1 in elements:
        current_seq += 1
        i = i+1
        current_seq_ele.append(i)

    if current_seq > max_seq:
        max_seq = current_seq
        seq_ele = current_seq_ele
    
    

print(max_seq, seq_ele)
