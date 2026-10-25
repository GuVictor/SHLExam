import sys


def extended_gcd(a, b):
    """Return (gcd, x, y) such that a*x + b*y = gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    return gcd, y1, x1 - (a // b) * y1


def ceil_div(numerator, denominator):
    """Return ceil(numerator / denominator) for a positive denominator."""
    return -((-numerator) // denominator)


def minimum_cost(num_apples, lot_a, price_a, lot_b, price_b):
    """Compute the minimum cost to buy exactly num_apples using the two lots."""
    if num_apples == 0:
        return 0

    gcd, x0, y0 = extended_gcd(lot_a, lot_b)
    if num_apples % gcd != 0:
        return -1

    scale = num_apples // gcd
    x0 *= scale
    y0 *= scale

    # Every other solution has the form:
    #   x = x0 + (lot_b // gcd) * t,  y = y0 - (lot_a // gcd) * t
    step_x = lot_b // gcd
    step_y = lot_a // gcd

    # The cost is linear in t, so it is minimized at an endpoint of the
    # feasible range where both x and y remain non-negative.
    t_min = ceil_div(-x0, step_x)
    t_max = y0 // step_y

    def cost(t):
        return price_a * (x0 + step_x * t) + price_b * (y0 - step_y * t)

    return min(cost(t_min), cost(t_max))


def main():
    data = sys.stdin.read().split()
    if len(data) < 5:
        return
    num_apples = int(data[0])
    lot_a = int(data[1])
    price_a = int(data[2])
    lot_b = int(data[3])
    price_b = int(data[4])

    print(minimum_cost(num_apples, lot_a, price_a, lot_b, price_b))


if __name__ == "__main__":
    main()
