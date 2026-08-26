'''
Finding the longest  sequence number length

output -> 4
'''
l = [100,200,2,3,4,41,42,43,44]

def longest_sequence(data):
    seq_len = 0
    for i in range(len(data)):
        # check if i-1 present in data if yes move one to next element in data 
        if data[i] - 1 in data:
            continue
        else:
            counter = data[i]
            current_len = 1
            while True: 
                next_ele = counter + 1
                if next_ele in data:
                    current_len += 1
                    counter = next_ele
                else:
                    break
            if current_len > seq_len:
                seq_len = current_len

    return seq_len

print(longest_sequence(l))
