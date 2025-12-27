import sys

def main():
    if len(sys.argv) < 2:
        print("Нужно передать путь к файлу")
        return

    filename = sys.argv[1]

    nums = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                nums.append(int(line.strip()))

    nums.sort()
    n = len(nums)

    # медиана
    if n % 2 == 1:
        target = nums[n // 2]
    else:
        target = nums[n // 2]  # можно взять любой из двух медианных

    moves = sum(abs(x - target) for x in nums)

    if moves > 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
    else:
        print(moves)

if __name__ == "__main__":
    main()
