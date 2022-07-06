
# impretative programming

s =[]
num = int(input("enter number of student "))
for i in range(num):
    marks = int(input("enter marks "))
    s.append(marks)
s.sort()
print("higest marks ",+s[-1]) 





nums = [11,2,3,4,5]
nums.append(10)
print(nums)
nums.sort()
print(nums)

# [11, 2, 3, 4, 5, 10]
# [2, 3, 4, 5, 10, 11]
