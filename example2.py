import math


arr = [1, 3, 2, 2, 4, 5]
target = 6

window_start, window_end = 0, 0
current_sum = 0
current_len = math.inf
result = None
# brute force
# for i in range(len(arr) - 1):
#     for j in range(i + 1, len(arr)):
#         current_sum += arr[i] + arr[j]
#         if current_sum == target and len(arr[i : j + 1]) < current_len:
#             result = arr[i : j + 1]
#             current_len = len(arr[i : j + 1])
#             current_sum = 0
# print(result)

while (window_start <= window_end) and (window_end < len(arr)):
    current_sum += arr[window_end]
    sub_len = len(arr[window_start : window_end + 1])
    if current_sum > target:
        current_sum -= arr[window_start]
        window_start += 1

    if current_sum == target and sub_len < current_len:
        result = arr[window_start : window_end + 1]
        current_sum -= arr[window_start]
        window_start += 1
        current_len = sub_len
    window_end += 1
print(result)
