def nrz_unipolar(data):
    result = []
    for b in data:
        if b == '1':
            result.append('+')
        else:
            result.append('0')
    return result


def nrz_l(data):
    result = []
    for b in data:
        if b == '0':
            result.append('+')
        else:
            result.append('-')
    return result


def nrz_i(data):
    result = []
    level = '+'

    for b in data:
        if b == '1':
            if level == '+':
                level = '-'
            else:
                level = '+'
        result.append(level)

    return result


def rz(data):
    result = []

    for b in data:
        if b == '1':
            result.append('+')
            result.append('0')
        else:
            result.append('-')
            result.append('0')

    return result


def manchester(data):
    result = []

    for b in data:
        if b == '1':
            result.append('-')
            result.append('+')
        else:
            result.append('+')
            result.append('-')

    return result


def diff_manchester(data):
    result = []
    level = '+'

    for b in data:
        if b == '0':
            if level == '+':
                level = '-'
            else:
                level = '+'

        result.append(level)

        if level == '+':
            level = '-'
        else:
            level = '+'

        result.append(level)

    return result


def ami(data):
    result = []
    level = '-'

    for b in data:
        if b == '1':
            if level == '+':
                level = '-'
            else:
                level = '+'
            result.append(level)
        else:
            result.append('0')

    return result


def pseudoternary(data):
    result = []
    level = '-'

    for b in data:
        if b == '0':
            if level == '+':
                level = '-'
            else:
                level = '+'
            result.append(level)
        else:
            result.append('0')

    return result


def draw(signal):
    print("\n+V :", end=" ")
    for s in signal:
        if s == '+':
            print("---", end=" ")
        else:
            print("   ", end=" ")
    print()

    print(" 0 :", end=" ")
    for s in signal:
        if s == '0':
            print("---", end=" ")
        else:
            print("   ", end=" ")
    print()

    print("-V :", end=" ")
    for s in signal:
        if s == '-':
            print("---", end=" ")
        else:
            print("   ", end=" ")
    print("\n")


while True:

    print("------ Line Encoding ------")
    print("1. NRZ-Unipolar")
    print("2. NRZ-L")
    print("3. NRZ-I")
    print("4. RZ")
    print("5. Manchester")
    print("6. Differential Manchester")
    print("7. AMI")
    print("8. Pseudoternary")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == '9':
        break

    data = input("Enter Binary Data: ")

    if choice == '1':
        draw(nrz_unipolar(data))

    elif choice == '2':
        draw(nrz_l(data))

    elif choice == '3':
        draw(nrz_i(data))

    elif choice == '4':
        draw(rz(data))

    elif choice == '5':
        draw(manchester(data))

    elif choice == '6':
        draw(diff_manchester(data))

    elif choice == '7':
        draw(ami(data))

    elif choice == '8':
        draw(pseudoternary(data))

    else:
        print("Invalid Choice")