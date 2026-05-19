rolex = 0
fossil = 0
casio = 0
titan = 0
timex = 0

questions = [
    "Do you like premium luxury items? ",
    "Do you attend formal events often? ",
    "Do you prefer classic watch designs? ",
    "Do you like sporty looks? ",
    "Do you want a watch for daily use? ",
    "Do you prefer affordable watches? ",
    "Do you like metal straps? ",
    "Do you like leather straps? ",
    "Do you travel frequently? ",
    "Do you prefer lightweight watches? ",
    "Do you like bold dial designs? ",
    "Do you wear watches mainly for fashion? ",
    "Do you like vintage style watches? ",
    "Do you prefer simple minimal designs? ",
    "Do you go to college or office daily? ",
    "Do you like durable watches? ",
    "Do you prefer branded accessories? ",
    "Do you like black dial watches? ",
    "Do you prefer elegant watches over sporty ones? ",
    "Do you want a long-lasting watch? "
]

print("Answer all questions with YES or NO\n")

for q in questions:

    ans = input(q).lower()

    if ans == "yes":

        # Rolex
        if q in [
            questions[0], questions[1], questions[6],
            questions[11], questions[16], questions[18]
        ]:
            rolex += 2

        # Fossil
        if q in [
            questions[2], questions[7], questions[10],
            questions[11], questions[12]
        ]:
            fossil += 2

        # Casio
        if q in [
            questions[3], questions[5], questions[9],
            questions[15], questions[19]
        ]:
            casio += 2

        # Titan
        if q in [
            questions[4], questions[13], questions[14],
            questions[18], questions[19]
        ]:
            titan += 2

        # Timex
        if q in [
            questions[5], questions[8], questions[9],
            questions[13], questions[15]
        ]:
            timex += 2

print("\n--- SCORES ---")
print("Rolex :", rolex)
print("Fossil:", fossil)
print("Casio :", casio)
print("Titan :", titan)
print("Timex :", timex)

maximum = max(rolex, fossil, casio, titan, timex)

print("\n--- RECOMMENDED WATCH ---")

if maximum == rolex:
    print("Recommended Watch Brand: ROLEX")
    print("Best for luxury, premium style, and elegance.")

elif maximum == fossil:
    print("Recommended Watch Brand: FOSSIL")
    print("Best for fashion and stylish casual wear.")

elif maximum == casio:
    print("Recommended Watch Brand: CASIO")
    print("Best for sporty, durable, and everyday use.")

elif maximum == titan:
    print("Recommended Watch Brand: TITAN")
    print("Best for office, formal, and minimal style.")

else:
    print("Recommended Watch Brand: TIMEX")
    print("Best for comfort, simplicity, and daily wear.")