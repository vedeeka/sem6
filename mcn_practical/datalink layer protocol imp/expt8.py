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