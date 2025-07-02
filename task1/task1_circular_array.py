import sys


def main():
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    start = 1
    for i in range(n):
        print(start, end='')
        start += m - 1
        if start > n:
            start = start % n
            if start == 0:
                start = n
        if start == 1:
            break
    print()


if __name__ == "__main__":
    main()
