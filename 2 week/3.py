mass1 = set(map(int, input().split()))
mass2 = set(map(int, input().split()))
res = sorted(mass1 & mass2)
if res:
    print("Общие элементы:", " ".join(map(str, res)))
else:
    print("Общих элементов нет")
