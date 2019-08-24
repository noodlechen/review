data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data)) #印出讀取進度
print('資料計有：', len(data), '筆') #印出資料筆數
print(data[0]) #印出第＿筆資料內容

sum_len = 0

for d in data:
	sum_len += len(d)
print('留言計有： ', sum_len, '字')
print('留言平均為：', sum_len / len(data), '字')

new = []
for d in data:
	if len(d) > 100:
		new.append(d)
print('共有', len(new), '筆留言大於100')

better = []
for d in data:
	if 'better' in d:
		better.append(d)
print('共有', len(better), '筆留言提到better')
print(better[2])

