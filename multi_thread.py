from threading import Thread
import time
import random
import queue

# counter = 0 # This counter is the shared state 

# def increment_counter():
# 	global counter
# 	time.sleep(random.randint(0, 2))
# 	counter += 1
# 	time.sleep(random.randint(0, 2))
# 	print(f'New counter value: {counter}')
# 	time.sleep(random.randint(0, 2))
# 	print('-----------')

# for x in range(10):
# 	t = Thread(target=increment_counter)
# 	time.sleep(random.randint(0, 2))
# 	t.start()
 
'''
For each iteration, we start a new thread that access the shared state. Due to the sleep, when Thread A is sleeping, Thread B would 
increment based on its initial global reading, not the current incremented by Thread A.

This is essentially a race condition where 2 or more threads access the same shared data 
and try to change it at the same time.
'''

# Instead, we would use a Queue to modify the shared data for multiple Threads.

counter1 = 0
job_queue = queue.Queue() # Things to print out 
counter_queue = queue.Queue() # Amount to increment Counter


def increment_manager():
	global counter1
	while True:
		increment = counter_queue.get()  # this waits until an item is available and locks the queue - This thread now has this resource
		time.sleep(random.random())
		old_counter = counter1
		time.sleep(random.random())
		counter1 = old_counter + increment
		time.sleep(random.random())
		job_queue.put((f'New counter value {counter1}', '------------'))
		time.sleep(random.random())
		counter_queue.task_done()  # Unlocks the queue - Another Thread can access 


# printer_manager and increment_manager run continuously because of the `daemon` flag - Runs forever in the BG
Thread(target=increment_manager, daemon=True).start()

def printer_manager():
	while True:
		for line in job_queue.get():
			time.sleep(random.random())
			print(line)
		job_queue.task_done()

# printer_manager and increment_manager run continuously because of the `daemon` flag.
Thread(target=printer_manager, daemon=True).start()

def increment_counter():
	counter_queue.put(1) 
	time.sleep(random.random())

worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
	time.sleep(random.random())
	thread.start()

for thread in worker_threads:
	thread.join()  # wait for it to finish

counter_queue.join()  # wait for counter_queue to be empty
job_queue.join()  # wait for job_queue to be empty