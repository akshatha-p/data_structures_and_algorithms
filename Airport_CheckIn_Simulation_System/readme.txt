Simulating a check-in operation for an airline company at an airport terminal

- Implementing a queue and using it to simulate the evolution of waiting queues. 
- There are two classes of service: first class and coach and each class has a dedicated queue.
- There are 3 service stations for first-class and 1 first-class queue.
- There are 4 coach service stations and and 1 coach queue.
- Each service station takes passengers from the corresponding queue, but if a first-class service station is free 
  and the queue for the coach is not empty then the service station serves passengers from the coach queue.
- Passenger arrival times are random, but subject to average arrival times.
- Passenger service times are also random, but subject to average service times
-The simulation starts with empty waiting queues and free service stations and the simulation ends when all the queues are empty and all the service stations are free.

Input to be given  
- The total simulation time or duration of the check-in. 
- The coach class: 
	- average arrival rate
	- average service rate
- The first-class:
	- average arrival rate 
	- average service rate

Output 

- The duration of the simulation (which may be longer than the input parameter, as when check-in closes, there may be passengers in the waiting queues and service stations).
- The maximum length of the queue for each queue.
- The average and maximum waiting time for each queue.
- The rate of occupancy of each service station 


