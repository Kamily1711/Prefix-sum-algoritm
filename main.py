n = int(input())
s = int(input())
vetor = [int(i) for i in input().split()]
prefix_sum = []
prefix_sum.append(vetor[0])
cont = 0
for x in range(1, len(vetor)):
    prefix_sum.append(prefix_sum[x-1]+vetor[x])
prefix_sum.sort(reverse=True)
for num1 in prefix_sum:
    if num1 == s:
        cont += 1
    for num2 in prefix_sum:
        if num1-num2 == s:
            cont += 1
print(cont)
