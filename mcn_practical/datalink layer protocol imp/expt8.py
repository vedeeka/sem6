import random

def selective_repeat(frames, window):
    ack = [False] * frames
    start = 0

    while start < frames:

        print("\nSending Window:")

        end = min(start + window, frames)

        for i in range(start, end):
            if not ack[i]:
                print("Frame", i, "sent")

                if random.choice([True, False]):
                    print("ACK received for Frame", i)
                    ack[i] = True
                else:
                    print("Frame", i, "lost")

        while start < frames and ack[start]:
            start += 1

        print("Sliding Window...\n")

frames = int(input("Enter total frames: "))
window = int(input("Enter window size: "))

selective_repeat(frames, window)





import random
def selective_repeat(data,ws):
    ack=[False]*data
    base=0

    while(base<data):
        end=min(base+ws,data)

        print("sending frame",base,end)
        i=base
        while(i<end):
            if ack[i]==False:
                print("sending data",i)

                got=random.choice([True,False])
                if got:
                    print("got frame",i)
                    ac=random.choice([True,False])
                    if ac:
                        print("ack recieved")
                        ack[i] = True
                        

                    else:
                        base=i
                        print("ack not recieved")
                                    

                else:
                    base=i
                    print("frame not got")
                
            i+=1
            
        k=0
        while k < len(ack) and ack[k]:
            k += 1
        base=k

selective_repeat(10,4)