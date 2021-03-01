

import random


## # class to define queue functionality



class Queue:
    def __init__(self):
        self.queue = [] 
    
    def enqueue(self,passenger):
        self.queue.append(passenger)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return True 
        return False
    def lenQ(self):
        lenQ = len(self.queue)
        return lenQ

## # Service station class 
## # Holds service time if a passenger is being served 
class svr_station:
    def __init__(self):
        #left_srv_time
        self.remainingST = 0
        self.servingP = None
    def isIdle(self):
        if self.remainingST == 0:
            return True
        return False

## # Passenger class 
## # Each passengers service time is uniformly distributed between 1 and 2*A+1 
## # with A being the service rate

class passg:
    def __init__(self,P_type,current_time,sr):
        self.type = P_type
        self.arrival = current_time
        self.service = self.rand_srvc_time(sr)
        
    def rand_srvc_time(self,A):
        n = random.randint(1,2*A+1)
        return n 

## # function to randomly select a passenger to of Coach or Frist Class
def coach_or_first(fc_ar, c_ar):
    fc_pass_rate = fc_ar/(fc_ar+c_ar)
    if random.random() <= fc_pass_rate:
        return 'f'
    else:
        return 'c'

## # creating passenger using the arrival rate 
## # uniformly distrbuted arrival time in the range (1, Arrival rate)
def new_passg(total_sim_duration,arrv_time,t):
    if random_num(arrv_time) == True and t < total_sim_duration:
        return True
def random_num(A):
    if random.random() <= 1.0/A :
        return True
    return False


if __name__ == "__main__":
        
    ## # taking input from user for total simulation duration, arrival and 
    ## # service rates for coach and first class
    sim_dur = int(input("Enter simulation duration: "))
    
    FC_AR = int(input("Enter average arrival rate for First class passengers: "))
    FC_SR = int(input("Enter average service rate for first class passengers: "))
    
    C_AR = int(input("Enter average arrival rate for coach class passengers: "))
    C_SR = int(input("Enter average service rate for coach class passengers: "))
    
    
    ## # Initializing passenger Queues 
    FC_q = Queue()
    C_q = Queue()
    
    ## # Initializing service stations 
    ## # First class
    FC_S1 = svr_station()
    FC_S2 = svr_station()
    FC_S3 = svr_station()
    ## # Coach
    C_S1 = svr_station()
    C_S2 = svr_station()
    C_S3 = svr_station()
    C_S4 = svr_station()
    
    ## # counter to keep track of number of passengers in each queue
    FCnum_p = 0
    Cnum_p = 0
    
    ## # maximum length of the queues
    
    max_lenFCq = 0
    max_lenCq = 0
    
    ## # maximum wait time in queue
    mwt_FCq = 0
    mwt_Cq = 0
    
    
    ## # total duration of each queue
    FCq_dur = 0
    Cq_dur = 0
    
    ## # time counter 
    duration = 0
    
    #service stations counter
    #first class 
    S1 = 0
    S2 = 0
    S3 = 0
    #coach class
    S4 = 0
    S5 = 0
    S6 = 0
    S7 = 0
    
    
    ## # run the simulation till run duration is less than user input simluation 
    ## # duration 
    ## # OR 
    ## # all of the stations have stopped serving passengers
    while duration < sim_dur or (
                not FC_q.isEmpty() and 
                not C_q.isEmpty() and 
                not FC_S1.isIdle() and 
                not FC_S2.isIdle() and 
                not C_S1.isIdle() and 
                not C_S2.isIdle() and 
                not C_S3.isIdle() and 
                not C_S4.isIdle()):
    ## # creating passengers and adding them to queue
    ## # first class queue 
        p_type = coach_or_first(FC_AR, C_AR)
        if p_type == 'f':
            if new_passg(sim_dur,FC_AR,duration):
                p = passg("f",duration,FC_SR)
                FC_q.enqueue(p)
                FCnum_p = FCnum_p + 1
                if FC_q.lenQ() > max_lenFCq :
                    max_lenFCq  = FC_q.lenQ()
    ## # coach class queue
        if p_type == 'c':
            if new_passg(sim_dur,C_AR,duration):
                p = passg("c",duration,C_SR)
                C_q.enqueue(p)
                Cnum_p = Cnum_p + 1
                if C_q.lenQ() > max_lenCq :
                    max_lenCq  = C_q.lenQ()
    
    ## # If a service stattion is free, it starts serving passengers.
    ## # If First class station is not serving and the first class queue is empty,
    ## # FC station will serve Coach 
    
    
    ## # serving passengers using first class service stations  
    ## # First class service station 1  
    ## # part1 when First class station is free
        if FC_S1.remainingST == 0:
            if not FC_q.isEmpty():
                FC_P = FC_q.dequeue()
                FC_S1.remainingST = FC_P.service
                FC_S1.servingP = FC_P 
                WT = duration - FC_P.arrival
                if WT > FCq_dur:
                    mwt_FCq = WT
                FCq_dur = FCq_dur + WT
                
    #FS1.2coach passengers being serviced in First class station 
    #when First Class q is Empty
            elif not C_q.isEmpty():
                C_P = C_q.dequeue()
                FC_S1.remainingST = C_P.service
                FC_S1.servingP = C_P        
                WT = duration - C_P.arrival
                if WT > Cq_dur:
                    mwt_Cq = WT
                Cq_dur = Cq_dur + WT
                
    #FS1.3 when First class station1 is servicing a passenger
        if FC_S1.remainingST > 1:
            FC_S1.remainingST = FC_S1.remainingST - 1
            S1 = S1 +1
        elif FC_S1.remainingST == 1:
            FC_S1.remainingST = 0
            p = FC_S1.servingP
            S1 = S1 + 1
            
    
    #first class service station2   
    #part1 when First class station2 is free        
        if FC_S2.remainingST == 0:
            if not FC_q.isEmpty():
                FC_P = FC_q.dequeue()
                FC_S2.remainingST = FC_P.service
                FC_S2.servingP = FC_P 
                WT = duration - FC_P.arrival
                if WT > FCq_dur:
                    mwt_FCq = WT
                FCq_dur = FCq_dur + WT
    
    #part2 coach passengers being serviced in First class station 
    #when First Class q is Empty                
            elif not C_q.isEmpty():
                C_P = C_q.dequeue()
                FC_S2.remainingST = C_P.service
                FC_S2.servingP = C_P
                WT = duration - C_P.arrival
                if WT > Cq_dur:
                    mwt_Cq = WT
                Cq_dur = Cq_dur + WT
                
    #part3 when First class station 2 is servicing a passenger
        if FC_S2.remainingST > 1:
            FC_S2.remainingST = FC_S2.remainingST - 1
            S2 = S2 +1         
        elif FC_S2.remainingST == 1:
            FC_S2.remainingST = 0
            p = FC_S2.servingP
            S2 = S2 + 1

    #first class service station3 
    # part1 when First class station3 is free          
        if FC_S3.remainingST == 0:
            if not FC_q.isEmpty():
                FC_P = FC_q.dequeue()
                FC_S3.remainingST = FC_P.service
                FC_S3.servingP = FC_P 
                WT = duration - FC_P.arrival
                if WT > FCq_dur:
                    mwt_FCq = WT
                FCq_dur = FCq_dur + WT
                
    #part2 coach passengers being serviced in First class station 
    #when First Class q is Empty            
            elif not C_q.isEmpty():
                C_P = C_q.dequeue()
                FC_S3.remainingST = C_P.service
                FC_S3.servingP = C_P
                WT = duration - C_P.arrival
                if WT > Cq_dur:
                    mwt_Cq = WT
                Cq_dur = Cq_dur + WT
                
    #part3 when First class station3 is servicing a passenger
        if FC_S3.remainingST > 1:
            FC_S3.remainingST = FC_S3.remainingST - 1
            S3 = S3 +1            
        elif FC_S3.remainingST == 1:
            FC_S3.remainingST = 0
            p = FC_S3.servingP
            S3 = S3 + 1
            

        ## # Coach Service Stations
        ## # coach Station 1
        ## # part1 when coach service station 1 is free
        if C_S1.remainingST == 0:
            if not C_q.isEmpty():
                C_P = C_q.dequeue()
                C_S1.remainingST = C_P.service
                C_S1.servingP = C_P
                WT = duration - C_P.arrival
                if WT > Cq_dur:
                    mwt_Cq = WT
                Cq_dur = Cq_dur + WT
                
    #part1 when coach service station 1 is serving a passenger
        if C_S1.remainingST > 1:
            C_S1.remainingST = C_S1.remainingST - 1
            S4 = S4 +1
        elif C_S1.remainingST == 1:
            C_S1.remainingST = 0
            p = C_S1.servingP
            S4 = S4 + 1 
            
            
    ## # coach Station 2    
    #part1 when coach service station 2 is free 
        if C_S2.remainingST == 0:
            if not C_q.isEmpty():
                C_P = C_q.dequeue()
                C_S2.remainingST = C_P.service
                C_S2.servingP = C_P
                WT = duration - C_P.arrival
                if WT > Cq_dur:
                    mwt_Cq = WT
                Cq_dur = Cq_dur + WT
                
    #part2 when coach service station 2 is serving a passenger
        if C_S2.remainingST > 1:
            C_S2.remainingST = C_S2.remainingST - 1
            S5 = S5 +1
        elif C_S2.remainingST == 1:
            C_S2.remainingST = 0
            p = C_S2.servingP
            S5 = S5 + 1 
            
            
     ## # coach Station 3       
    #part1 when coach service station 3 is free
        if C_S3.remainingST == 0:
            if not C_q.isEmpty():
                C_P = C_q.dequeue()
                C_S3.remainingST = C_P.service
                C_S3.servingP = C_P
                WT = duration - C_P.arrival
                if WT > Cq_dur:
                    mwt_Cq = WT
                Cq_dur = Cq_dur + WT
                
    #part2 when coach service station 3 is serving a passenger
        if C_S3.remainingST > 1:
            C_S3.remainingST = C_S3.remainingST - 1
            S6 = S6 +1
        elif C_S3.remainingST == 1:
            C_S3.remainingST = 0
            p = C_S3.servingP
            S6 = S6 + 1 
            
            
      ## # coach Station 3         
    #part1 when coach service station 4 is free
        if C_S4.remainingST == 0:
            if not C_q.isEmpty():
                C_P = C_q.dequeue()
                C_S4.remainingST = C_P.service
                C_S4.servingP = C_P
                WT = duration - C_P.arrival
                if WT > Cq_dur:
                    mwt_Cq = WT
                Cq_dur = Cq_dur + WT
                
    #part2 when coach service station 4 is serving a passenger
        if C_S4.remainingST > 1:
            C_S4.remainingST = C_S4.remainingST - 1
            S7 = S7 +1
        elif C_S4.remainingST == 1:
            C_S4.remainingST = 0
            p = C_S4.servingP
            S7 = S7 + 1  
        duration = duration + 1
        
    #outputs
    print("Total duration is:",duration)
    print("")
    
    #max queue length
    print("Max queue length of First class:",max_lenFCq)
    print("Max queue length of coach class:",max_lenCq)
    print("")
    
    # calculating average wait time by dividing the total simulated duration 
    # by the number of passengers in first class and coach class
    FC_awt = duration/FCnum_p
    C_awt = duration/Cnum_p
    
    #average wait time 
    print("Average wait time of first class queue: ",round(FC_awt,2))
    print("Average wait time of coach class queue: ",round(C_awt,2))
    print("")
    
    #wait time
    print("Maximum wait time of First class:",mwt_FCq)
    print("Maximum wait time of coach class:",mwt_Cq)
    print("")
    
    # rate of occupancy calculation is obtained by 
    # diving the counter of each station by the total duration 
    OR_FC_S1 = (S1/duration)*100
    print("Rate of occupancy of First Class station1:",round(OR_FC_S1,2))
    OR_FC_S2 = (S2/duration)*100
    print("Rate of occupancy of First Class station2:",round(OR_FC_S2,2))
    OR_FC_S3 = (S3/duration)*100
    print("Rate of occupancy of First Class station3:",round(OR_FC_S3,2))
    print("")
    
    OR_C_S1 = (S4/duration)*100
    print("rate of occupancy of Coach Class station1:",round(OR_C_S1,2))
    OR_C_S2 = (S5/duration)*100
    print("rate of occupancy of Coach Class station2:",round(OR_C_S2,2))
    OR_C_S3 = (S6/duration)*100
    print("rate of occupancy of Coach Class station3:",round(OR_C_S3,2))
    OR_C_S4 = (S7/duration)*100
    print("rate of occupancy of Coach Class station4:",round(OR_C_S4,2))
    
    
    
