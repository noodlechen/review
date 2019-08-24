data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data)) #印出讀取進度

print(len(data)) #印出資料筆數
print(data[0]) #印出第＿筆資料內容