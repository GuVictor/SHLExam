# Minimum Cost of Exactly N Apples

## Problem Description

Josh went to the market to buy `N` apples. He found two shops, A and B, that sold apples in lots. He can buy any number of complete lots but cannot buy loose apples. He is confused about the price and needs help calculating the minimum cost of exactly `N` apples.

Write an algorithm for Josh to calculate the minimum cost of exactly `N` apples.

## Input

The input consists of five lines:

1. An integer `num`, representing the total number of apples Josh wishes to buy (`N`).
2. A positive integer `appleShop1`, representing the number of apples in one lot from shop A.
3. A positive integer `priceShop1`, representing the price of one lot at shop A.
4. A positive integer `appleShop2`, representing the number of apples in one lot from shop B.
5. A positive integer `priceShop2`, representing the price of one lot at shop B.

## Output

Print a positive integer representing the minimum price at which Josh can buy exactly `N` apples.

## Constraints

- `0 ≤ num, priceShop1, priceShop2`
- `1 ≤ appleShop1, appleShop2`

## Note

- There will always be at least one solution.
- There is only one lot size for a particular shop.
- There is an unlimited supply of apples at both shops.

## Example

### Input
```text
19
3
10
4
15
```

### Output
```text
65
```

### Explanation

Josh can buy five lots from the first shop and one lot from the second shop, for a total cost of `5 × 10 + 15 = 65`.
