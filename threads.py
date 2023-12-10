import time 
from threading import Thread

# We can create a Thread from the OS and allow us to run another piece of code in the Thread

def ask_user(): # This is a blocking operation - We must wait for the I/O. We want other background functions to run too.
    start = time.time()
    user_input = input("Enter Your Name")
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time - start}')
    
def complex_calc():
    start = time.time()
    print("Calculating...")
    [x**2 for x in range(200000)]
    print(f'Complex : {time.time() - start}')

thread1 = Thread(target=complex_calc) # We pass the function into the Thread 
thread2 = Thread(target=ask_user)

start = time.time()
thread1.start() # Start the threads
thread2.start()

thread1.join() 
thread2.join() # Tells the main thread to wait for Thread1/2 to finish before. These are waiting operations since we force to wait!
print(f'Timing : {time.time() - start}')


# Creates 2 Threads that run the same thing - Note that this is ineffecient!
# One thread can run at a time - This way would make Python pull in and pull out the theeads - Overhead!   
thread3 = Thread(target=complex_calc)
thread4 = Thread(target=complex_calc)


'''
Note that the inefficiency comes from using the CPU. 

If we use CPU depedendent operations such as calculations, then using Threads on 2 computational heavy 
functions would slow down the code! 


Instead, for operations such as prompting for an User Input and we want to run a one computationally heavy process,
then Threads is recommended!
'''