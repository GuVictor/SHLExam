from collections import deque
import sys


def find_first_meat_orders(order_numbers, window_size):
    """Return the first meat pizza (negative number) in each sliding window.

    A monotonic deque stores the indices of negative numbers currently
    inside the window, so its front always holds the first meat order.
    """
    total_orders = len(order_numbers)
    if window_size <= 0 or total_orders == 0:
        return []

    negative_indices = deque()
    result = []

    for index in range(total_orders):
        if order_numbers[index] < 0:
            negative_indices.append(index)

        # Drop negative indices that have already left the current window.
        while negative_indices and negative_indices[0] <= index - window_size:
            negative_indices.popleft()

        if index >= window_size - 1:
            if negative_indices:
                result.append(order_numbers[negative_indices[0]])
            else:
                result.append(0)

    return result


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    total_orders = int(data[0])
    order_numbers = list(map(int, data[1:1 + total_orders]))
    window_size = int(data[1 + total_orders])

    result = find_first_meat_orders(order_numbers, window_size)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
