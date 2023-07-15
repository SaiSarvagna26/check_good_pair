def check_good_pair(A, B):
    seen = set()

    for num in A:
        complement = B - num
        if complement in seen:
            return 1
        seen.add(num)

    return 0

A = list(map(int,input().split()))
B = int(input())
result = check_good_pair(A, B)
print(result) 

