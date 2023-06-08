#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_argument = len(sys.argv) - 1

    if num_argument == 0:
        print("0 arguments.")
    elif num_argument == 1:
        print("1 argument:")
    else:
        print("{} argument:".format(num_argument))

    for i in range(num_argument):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
