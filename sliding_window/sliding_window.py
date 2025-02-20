def sliding_window_fixed(input, window_size):
    ans = window = input[0:window_size]
    for right in range(window_size, len(input)):
        left = right - window_size
        window.pop(input[left])
        window.append(input[right])
        ans = max(ans, window) # depending on the question
    return ans

def invalid(dict):
    return False

def sliding_window_flexible_longest(input):
    window = {}
    ans = 0
    left = 0
    for right in range(len(input)):
        window.append(input[right])
        while invalid(window):  # update left until window is valid again
            window.pop(input[left])
            left += 1
        ans = max(ans, window)        # window is guaranteed to be valid here
    return ans
