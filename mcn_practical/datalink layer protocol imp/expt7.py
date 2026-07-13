import random
import time
def go_back_n(total_frames, window_size):
    base = 0
    next_frame = 0
    while base < total_frames:
        while next_frame < base + window_size and next_frame < total_frames:
            print("Sender: Sending Frame", next_frame)
            next_frame += 1
            time.sleep(0.5)
        ack = random.randint(base, next_frame)
        if ack < next_frame:
            print("Receiver: ACK received for Frame", ack)
            base = ack + 1
        else:
            print("Error occurred! Frame lost.")
            print("Sender: Go back to Frame", base)
        time.sleep(1)
frames = int(input("Enter total number of frames: "))
window = int(input("Enter window size: "))
go_back_n(frames, window)
