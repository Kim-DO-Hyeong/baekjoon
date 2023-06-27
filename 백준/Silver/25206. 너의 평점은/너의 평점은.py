dict_a = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0,
    'P':0.0
}

listScore = []

for i in range(20):
    score = list(input().split())
    listScore.append(score)

sum = 0
sum_h = 0
for i in listScore:
    if i[2] == 'P':
        continue
    sum = sum + (float(i[1]) * dict_a[i[2]])
    sum_h += float(i[1])

print("{:6f}".format(sum/sum_h))