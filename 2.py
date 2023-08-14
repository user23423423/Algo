a = list(map(int, input().split()))

end = len(a) - 1
for i in range(len(a)):
        if a[i] > a[end]:
            a[i], a[end] = a[end], a[i]
            end -= 1
print(a)


