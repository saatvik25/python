# split an array in odd and even


def split(mix):
    evenli =[]
    oddli =[]
    
    for i in mix:
        if(i%2==0):
            evenli.append(i)
        else:
            oddli.append(i)


    print("even list is  ",evenli)   
    print("odd list is  ",oddli)
arr = [1,2,4,3,6,5,7,8,9,0] 
split(arr)
            
# even list is   [2, 4, 6, 8, 0]
# odd list is   [1, 3, 5, 7, 9]

