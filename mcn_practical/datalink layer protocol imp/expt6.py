import random
import time
def stop_and_wait_arq(total_frames):
    frame = 0
    while frame < total_frames:
        print("\nSender: Sending Frame", frame)
        time.sleep(1)
        ack_received = random.choice([True, False])
        if ack_received:
            print("Receiver: Frame", frame, "received")
            print("Receiver: Sending ACK", frame)
            time.sleep(1)
            print("Sender: ACK", frame, "received")
            frame += 1
        else:
            print("Receiver: Frame lost or ACK lost")
            print("Sender: Timeout occurred")
            print("Sender: Retransmitting Frame", frame)

n = int(input("Enter number of frames to send: "))
stop_and_wait_arq(n)









import random
import time


def stop_and_wait_arq(total_frames):

    frame = 0


    while frame < total_frames:


        print("\nSender: Sending Frame", frame)
        time.sleep(1)

    
        frame_received = random.choice([True, False])

        if frame_received:

            print(f"Receiver: Frame {frame} received")


            print(f"Receiver: Sending ACK {frame}")
            time.sleep(1)

 
            ack_received = random.choice([True, False])

            if ack_received:

                print(f"Sender: ACK {frame} received")


                frame += 1

            else:

                print(f"ACK {frame} lost")
                print("Sender: Timeout occurred")
                print(f"Sender: Retransmitting Frame {frame}")

        else:

            print(f"Receiver: Frame {frame} lost")
            print("Sender: Timeout occurred")
            print(f"Sender: Retransmitting Frame {frame}")


n = int(input("Enter number of frames to send: "))

stop_and_wait_arq(n)