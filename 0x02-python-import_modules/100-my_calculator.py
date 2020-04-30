#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    from sys import argv

    leng = len(argv)
    if (leng != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = argv[1]
    b = argv[3]
    operator = [['+', cal.add], ['-', cal.sub], ['*', cal.mul], ['/', cal.div]]

    for i in operator:
        if (i[0] == argv[2]):
            print("{0} {1} {2} = {3}".
                  format(a, i[0], b, i[1](int(a), int(b))))
            exit(0)

    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
