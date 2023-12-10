Processes and Threads 

1. Each Computer has Cores, which they run one process in it. Each Core is relatively independent but can communicate to each other.
Most computer runs on a Single Core.


2. Thread is a line of code execution, that is ran in one core at a time. 
Waiting Threads are those that are waiting to be executed. 


3. A process is a wrapper if the Core and Thread that contains at least one Thread and some resources set aside by the OS.
It mamnages all the resources that the thread needs to run.
A process can contain multiple cores. Really depends on how we define what is being wrapped.


4. Time Slicing - Taking a Thread of a Core and replacing it with another. It is potentially costly since the OS saves the state of the previous thread that was running such that it does not start from the head again. 


Python Global Interpretator Lock


1. When we launch an app, we get a new Python Process. In this process, we have the Main Thread (But we can make more). 


2. Note that we only run a single thread in a single core. Python implementation does not allow us the run 2 threads in one process at the same time. This is due to each thread needing a key resource that is singular for the thread to run. 


3. This resource is the GIL. 


4. We can open different Python Apps that can run simultaenously, since we can launch multiple process at the same time - With each process having a GIL. However, we cant make these different processes to communicate with each other. 


Point of Threads (Reduce Waiting Time)


1. Having a Single Threads would delay our programme, such as thsoe delayed by User's I/O inputs etc. 


2. Instead if we release the GIL, we would allow for non stopping operations. Our threads are only running when there are things to do! 


3. We do not have to wait for the User's Input but instead perform other operations in the mean time.


4. Note that if all threads are doing things, then multiple threads are not effective. Since Python does poorly in parallel computing.