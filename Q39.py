#On a certain train, Chef-the ticket collector, collects a fine of Rs. X if a passenger is travelling without a ticket.
#It is known that a passenger carries either a single ticket or no ticket. P passengers are travelling and they have a total of 
#Q tickets. Help Chef calculate the total fine collected.


t=int(input())
for i in range(t):
    X,P,Q=map(int,input(),split())
        print((P-Q)*X)
   
