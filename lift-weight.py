#-----------------------------Elevator program---------------------------------------
l2=0
class lift:
    def __init__(self,c):
        self.c=c

 # erasing txt file just in case need reset
    def erasing(self):
        import os
        if os.path.exists("floor.txt"):
            os.remove("floor.txt")
        else:
            print("File doesnot exist !")
# timer for lift door
    def countdown(self,t):
        import time
        while t >= 0:
            print(f"lift will close after {t} seconds")
            time.sleep(1)
            t -= 1
        print("Door is closing")



#switch to close and reopen door

    #def switch(self):
      #  o=input("press 'o' to open door: ")
       # if o== 'o':
           # self.countdown(t)
        #else:
         #   print( "Lift door is closing.")


# creating first entry; right after installing this elevator ideally lift will be in ground position.
    def file_write(self):
        f = open("floor.txt", "w")
        f.write("0")
        f.close()

# Reading last value/line from floor.txt file; last value= last positin of lift from where it need to move
    def floor_reader(self):
        with open('floor.txt', 'r') as f0:
            global l2
            (l2) = int(f0.readlines()[-1])
           # print(l2)
        f0.close()

# Adding values into floor.txt file and storing that value to l2
    def floor_adding(self):
        f2 = open("floor.txt", "a")
        f2.write('\n' + repr(self.d))
        f2.close()

#code to run if you want to go up(comming to your current floor)
    def comming(self,l2):
        if self.c < p:
            q = l2 - self.c
            print(f"lift is at {l2} th floor.")
            while self.c < l2:
                l2 -= 1
                if self.c < l2:
                    print(f" Lift is at {l2}th floor,going to {self.c} th floor.")
                else:
                    print(f"Welcome, you are at{self.c} th floor. ")

            q -= 1

        elif l2 == self.c:
            pass

        else:
            q = self.c - l2
            print(f"lift is at {l2}th floor.")
            while l2 < self.c:
                l2 += 1
                if self.c > l2:
                    print(f"Lift is at {l2}th floor,going to {self.c} floor.")
                else:
                    print(f"Welcome, you are at {self.c} th floor.")

            q -= 1
#over weight checker
    def over(self):
        import random
        r= random.randint(0,10)
        if r+1==10:
            print("Alert: over weight!!, maximum capacity of lift is 10 people.")
        else:
            pass


class elevator(lift):
    #global l2
    def __init__(self,c,d):
        self.d=d
        lift.__init__(self,c)

#lift going up to destination.

    def up(self, l2):

        if self.c < self.d:
            q = self.d - self.c
            # print(f"lift is at {self.c}th floor.")
            while self.c < self.d:
                self.c += 1
                l2 = self.d
                if self.c < self.d:
                    print(f" Lift is at {self.c}th floor,going to {self.d} th floor.")
                else:
                    print(f"Welcome,you are at {self.d} th floor.")
            q -= 1
# lift going down to the destination

    def down(self,l2):
        if self.c > self.d:
            q = self.c - self.d
            print(f"lift is at {self.c}th floor.")
            while self.d < self.c:
                self.c -= 1
                if self.d < self.c:
                    print(f"Lift is at {self.c}th floor.going to {self.d} th floor.")
                else:
                    print(f"Welcome, you are at {self.d} th floor.")
            q -= 1
            l2 = self.d
# --------------Using class to run program------------------------------
w=50
e=50
t=5
k=50
c1 = int(input("Enter your current floor: "))
lift1=lift(c1)
lift1.file_write()
lift1.floor_reader()
p=l2
lift1.comming(p)
print('Door is open ')
lift1.countdown(t)
lift1.over()
d1=int(input("Enter your destination: "))
lift1=elevator(c1,d1)
if c1 > d1:
    lift1.down(p)
    print('Door is open ')
    lift1.countdown(t)
    lift1.over()
    lift1.floor_adding()
    lift1.floor_reader()

elif c1 < d1:
    lift1.up(p)
    print('Door is open ')
    lift1.countdown(t)
    lift1.over()
    lift1.floor_adding()
    lift1.floor_reader()


for w in range (50):
    c = int(input("Enter your current floor: "))
    lift2 = lift(c)
    lift2.floor_reader()
    p = l2
    lift2.comming(p)
    print('Door is open ')
    lift2.countdown(t)
    lift2.over()
    d=int(input("Enter your destination : "))
    lift2=elevator(c,d)
    if c > d:
        lift2.down(p)
        print('Door is open ')
        lift2.countdown(t)
        lift2.over()
        lift2.floor_adding()
        lift2.floor_reader()

    elif c < d:
        lift2.up(p)
        print('Door is open ')
        lift2.countdown(t)
        lift2.over()
        lift2.floor_adding()
        lift2.floor_reader()





