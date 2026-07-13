import random
import time
def selective_repeat(total_frames, window_size):
    sender_base = 0
    receiver_buffer = [False] * total_frames
    while sender_base < total_frames:
        for frame in range(sender_base, min(sender_base + window_size, total_frames)):
            if not receiver_buffer[frame]:
                print("Sender: Sending Frame", frame)
                time.sleep(0.5)
                received = random.choice([True, False])
                if received:
                    print("Receiver: Frame", frame, "received")
                    print("Receiver: Sending ACK", frame)
                    receiver_buffer[frame] = True
                else:
                    print("Receiver: Frame", frame, "lost")
        while sender_base < total_frames and receiver_buffer[sender_base]:
            sender_base += 1
        print("Sliding window...\n")
        time.sleep(1)
frames = int(input("Enter total number of frames: "))
window = int(input("Enter window size: "))
selective_repeat(frames, window)
