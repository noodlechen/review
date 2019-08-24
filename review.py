data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data)) #印出讀取進度
print('資料計有：', len(data), '筆') #印出資料筆數


sum_len = 0

for d in data:
	sum_len += len(d)
print('留言計有： ', sum_len, '字')
print('留言平均為：', sum_len / len(data), '字')


print(data[0]) #印出第＿筆資料內容