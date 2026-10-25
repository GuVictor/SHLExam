# Maximum Salary

## Problem Description

Stephen is doing an internship in a company for `N` days. Each day, he may choose either an easy task or a difficult task. He may also choose to perform no task at all.

He chooses a difficult task on days when and only when he did not perform any work the previous day.

The amount paid by the company for both the easy and difficult tasks can vary each day, but the company always pays more for difficult tasks.

Write an algorithm to help Stephen earn the maximum salary.

## Input

The first line of the input consists of two space-separated integers, `num` and `type`, representing the number of days of the internship (`N`) and the types of tasks available for each day (`M`). The value of `type` (`M`) is always equal to `2`.

The next `N` lines consist of `M` space-separated integers: `easy` and `hard`, representing the amount paid for the easy task and the difficult task on that day, respectively.

## Output

Print an integer representing the maximum salary that Stephen can earn.

## Constraints

- `1 ≤ num ≤ 10^5`
- `type = 2`
- `2 ≤ hard ≤ 10^4`
- `1 ≤ easy < hard`

## Example

### Input
```text
4 2
1 2
4 10
20 21
2 23
```
