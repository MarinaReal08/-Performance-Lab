import sys

def get_path(n, m):
    path = []
    pos = 0  # начинаем с элемента 1 (индекс 0)
    step = m - 1  # шаг = m-1

    while True:
        path.append(str(pos + 1))
        pos = (pos + step) % n
        if pos == 0:
            break

    return "".join(path)


def main():
    if len(sys.argv) < 5:
        print("Необходимо передать параметры: n1 m1 n2 m2")
        return

    n1, m1, n2, m2 = map(int, sys.argv[1:5])
    print(get_path(n1, m1) + get_path(n2, m2))


if __name__ == "__main__":
    main()

