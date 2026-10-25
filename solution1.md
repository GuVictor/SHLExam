# Pizza Order Display — First Meat Pizza Order

## Problem Description

A pizza shop serves both vegan pizza and meat pizza. Customers place `N` orders at the shop. Their order numbers are printed on their bills.

The shop displays `K` out of the `N` orders (both vegan and meat) on its display screen at any time. The pizza shop is very famous and receives many orders. To avoid confusion, vegan pizza orders are represented by positive numbers, and meat pizza orders are represented by negative numbers on the screen.

The orders are served in the order in which they are displayed on the screen. Each time an order is ready, its number is removed from the display screen and a new order is added to the display at the end of the list.

A couple has arrived with their child Billy. Billy is a very naughty child. To keep him occupied, his parents tell him to make a list of the first meat pizza that appears in each set of `K` orders displayed on the shop's display screen.

Write an algorithm to help Billy make a list of the first meat-based pizza order numbers displayed on the screen each time an order is delivered to a customer.

## Input

- The first line contains an integer `orderPlaced_size`, representing the total number of orders placed (`N`).
- The second line contains `N` space-separated integers representing the vegan and meat pizza order numbers of the orders placed by customers.
- The last line contains an integer `size`, representing the number of orders displayed on the screen (`K`).

## Output

Print space-separated integers representing the first meat pizza order of every `K` orders displayed on the screen each time an order is delivered to a customer. Print `0` if the screen does not display any meat pizza order.

## Constraints

- `0 ≤ orderPlaced_size ≤ 10^6`
- `0 ≤ size ≤ orderPlaced_size`
- `-10^9 ≤ order numbers of the orders placed ≤ 10^9`

## Example

### Input
```text
6
-11 -2 19 37 64 -18
3
```

### Output
```text
-11 -2 0 -18
```

## Explanation

**Step 1:** At the time of the first display, the order numbers displayed are `[-11, -2, 19]`.  
So, the first displayed meat pizza order number is `-11`.

**Step 2:** At the time of the next display, the order numbers displayed are `[-2, 19, 37]`.  
So, the first displayed meat pizza order number is `-2`.

**Step 3:** At the time of the next display, the order numbers displayed are `[19, 37, 64]`.  
Since no meat-based pizza order is displayed, the output is `0`.

**Step 4:** Similarly, at the time of the next display, the order numbers displayed are `[37, 64, -18]`.  
So, the first displayed meat pizza order number is `-18`.

Therefore, the output is `[-11, -2, 0, -18]`.
