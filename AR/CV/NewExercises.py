import numpy as np

def One(): 
    array = np.zeros(10)

def Two(): 
    array = np.zeros(10)
    array[5] = 1

def Three():
    array = np.arange(10, 50)

def Four(): 
    array = np.arange(1, 10)
    array = array.reshape((3, 3))

def Five(): 
    array = np.arange(1,10)
    array = array.reshape((3, 3))
    array = np.flip(array, 1)
    print(array)

def Six(): 
    array = np.arange(1,10)
    array = array.reshape((3, 3))
    array = np.flip(array, 0)

def Seven(): 
    array = np.identity(3)

def Eigth(): 
    arr = np.random.seed(101) 
    arr = np.random.random_sample((0, 10))  
    print(arr)

def NeinNeinNein(): 
    arr = np.random.seed(101);  
    arr = np.random.randint(0, 100, 10); 
    print(np.mean(arr))
    
def Ten(): 
    arr = np.ones(shape=(10, 10)); 
    arr[1:9, 1:9] = 0; 
    
def Eleven(): 
    arr = np.zeros((5, 5))
    arr[:] = np.arange(1, 6)
    print(arr)
 
 
