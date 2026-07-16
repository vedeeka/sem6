import random
import time


def go_back_n(frames, window):
    i = 0

    while i < frames:
        print("\nSending Window:")
        end = min(i + window, frames)

        for j in range(i, end):
            print("Frame", j, "sent")

        # Randomly decide if a frame is lost
        lost = random.choice([True, False])

        if lost:
            lost_frame = random.randint(i, end - 1)
            print("Frame", lost_frame, "lost!")
            print("Resending from Frame", lost_frame)
            i = lost_frame
        else:
            print("All frames acknowledged.")
            i = end
frames = int(input("Enter total number of frames: "))
window = int(input("Enter window size: "))
go_back_n(frames, window)
