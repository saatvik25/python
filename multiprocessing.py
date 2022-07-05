


import multiprocessing
import time

result = []

def square(n):
    for i in n:
        time.sleep(0.5)
        print("square is ",+ i*i)
    
def cube(n):
    for i in n:
        time.sleep(0.90)
        print("cube is ",+ i*i*i)
    
if __name__ == "__main__":
    arr = [11,2,3,4]
    t1 = multiprocessing.Process(target = square , args = (arr,))
    t2 = multiprocessing.Process(target = cube , args = (arr,))
    
    t1.start()
    t2.start()
    
    #  when t1 t2 completes then only done is print
    t1.join()
    t2.join()    
    
    print("done")
    
        
    
   #output 
# square is  121
# cube is  1331
# square is  4
# square is  9
# cube is  8
# square is  16
# cube is  27
# cube is  64
# done
    
    
