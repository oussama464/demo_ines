from audioop import avg
from functools import lru_cache


# Example usage:
arr = [1, 2, 3, 4, 5]
k = 3
window_start = 0
window_sum = 0.0
avgs = []
# for i in range(len(arr) - k + 1):
#     sum = 0
#     for j in range(k):
#         sum += arr[i + j]
#     avgs.append(sum / k)
# print(avgs)

# add an elemnt at the window end
# calculate the avg an append
# check if the window size is greater or equal to k
# remove the element at window start from the window and increment
for window_end in range(len(arr)):
    window_sum += arr[window_end]
    if window_end >= k - 1:
        avgs.append(window_sum / k)
        window_sum -= arr[window_start]
        window_start += 1

print(avgs)
