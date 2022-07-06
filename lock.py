# implement concurrent programming using lock


import threading 
x=0
count =10
lock = threading.Lock()

def inc():
    global x
    lock.acquire()
    print("lock is aquired ")
    for i in range(count):
       
        x = x+1
        print(x)
    lock.release()
    print("lock is released ")  
    
def dec():
    global x
    lock.acquire()
    print("lock is aquired ")
    for i in range(count):
       
        x = x-1
        print(x)
    lock.release()
    print("lock is released ")  
        
    
    
t1 = threading.Thread(target = inc) 
t2 = threading.Thread(target = dec) 
t1.start()
t2.start()

    
    
    
#     lock is aquired 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# lock is released 
# lock is aquired 
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# lock is released 


    
        
