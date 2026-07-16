import random

def selective_repeat(frames, window):
    ack = [False] * frames

    while False in ack:

        print("\nSending Window:")
        for i in range(frames):
            if not ack[i]:
                print("Frame", i, "sent")

                if random.choice([True, False]):
                    print("ACK received for Frame", i)
                    ack[i] = True
                else:
                    print("Frame", i, "lost")

            # Stop after one window
            if i == window - 1:
                break

        print("Sliding Window...\n")

frames = int(input("Enter total frames: "))
window = int(input("Enter window size: "))

selective_repeat(frames, window)