# find the minimum lenght sublist whose element sum == 7 

#my first solution without any help works for all positve input 
list = [2,3,1,2,4,3]

minum_length = len(list)
min_sub_list = []

list_len = len(list)

for i in range(list_len):

    sub_list = []

    for j in range(i, list_len):
        sums = 0
        for k in sub_list:
            sums = sums + k

        if sums < 7:
            sub_list.append(list[j])
        
    length = len(sub_list)

    sum_sub_array = 0
    for ele in sub_list:
        sum_sub_array = sum_sub_array + ele

    if length < minum_length and sum_sub_array == 7:
        minum_length = length
        min_sub_list = sub_list

print(minum_length, min_sub_list)

#second solution optimized version with the help of chatgpt
nums = [2,3,1,2,4,3]
target = 7

left = 0
current_sum = 0
best_sublist = []
min_lenght = len(nums)

for right in range(len(nums)):
    current_sum = current_sum + nums[right]

    while current_sum >= target:

        if current_sum == target:
            length = right - left + 1

            if length < min_lenght:
                min_lenght = length
                best_sublist = nums[left:right+1]

        current_sum = current_sum - nums[left]
        left = left + 1

if best_sublist:
    print(min_lenght, best_sublist)
else:
    print("No subarray found")

#third solution that work for all inputs 
