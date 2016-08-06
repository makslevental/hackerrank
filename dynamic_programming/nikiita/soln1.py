import sys
import math
sys.stdin = open("/home/maksim/dev_projects/hackerrank/dynamic_programming/nikiita/input/input07.txt", "r")
# Recursive Solution: Calculate the sum first time and divide by 2, now start from first index and
# keep adding elements till you get (sum/2),thats your partition,now send both partitons in
# same function and find maximum between two. Special case when string is all '0's in that 
# case its just len(elementlist)-1. I am sending sum as parameter to avoid further sum calculations from list
def findMaxMoves(ele, sum):
    if sum % 2 != 0:
        return 0
    sum = sum / 2
    if sum == 0:
        if ele != len(ele) * [0]:  # not equal all zeroes and only one 1 floating around (no partitions possible)
            return 0
        else:
            return len(ele) - 1  # can partition as much as you want
    s = 0
    i = 0
    n = len(ele)
    if n <= 1:
        return 0
    while s != sum and i < n:
        s += ele[i]
        i += 1
    if i >= n:
        return 0
    else:
        return 1 + max(findMaxMoves(ele[0:i], sum), findMaxMoves(ele[i:n], sum))

def main():
    T = int(input().strip())
    for i in range(T):
        N = input()
        ele = list(map(int, input().strip().split()))
        print(findMaxMoves(ele, sum(ele)))
main()
