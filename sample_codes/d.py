# 1
marks = [15,16,14,19]
file = open('fg.txt','r+')

split_content = file.readlines()
for index, mark in enumerate(split_content):
    split_content[index] += str(marks[index])


f = " ".join(split_content).replace('\n','')
print(f)
file.write(f)

# 2 counting words in a file