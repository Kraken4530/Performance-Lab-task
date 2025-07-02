import sys


def main():
    file_with_array = sys.argv[1]
    nums = []
    with open(file_with_array, "r") as f:
        for line in f:
            if line.strip():
                nums.append(int(line.strip()))
    nums.sort()
    mediana = nums[(len(nums)-1)//2]
    result = 0
    for i in nums:
        result += abs(i - mediana)
    print(result)


if __name__ == "__main__":
    main()
