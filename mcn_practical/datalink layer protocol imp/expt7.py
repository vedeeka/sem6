import random

def go_back_n(frames, window):
    base = 1
    lost_once = []

    while base <= frames:

        end = min(base + window - 1, frames)

        print("\nCurrent Window:", end=" ")
        for i in range(base, end + 1):
            print(i, end=" ")
        print()

        for i in range(base, end + 1):
            print("Sending Frame", i)


            if i not in lost_once and random.choice([True, False]):
                print("Frame", i, "Lost!")
                print("Receiver discards remaining frames.")
                print("Go Back to Frame", i)
                lost_once.append(i)
                base = i
                break

            else:
                print("ACK", i, "Received")

        else:
            base = end + 1

    print("\nAll Frames Successfully Transmitted.")

frames = int(input("Enter Total Frames: "))
window = int(input("Enter Window Size: "))

go_back_n(frames, window)