import sys

def main():
    if len(sys.argv) < 3:
        print("Нужно передать два файла")
        return

    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    # читаем центр и радиусы
    with open(ellipse_file) as f:
        xc, yc = map(float, f.readline().split())
        a, b = map(float, f.readline().split())

    eps = 1e-9

    # читаем точки и проверяем каждую
    with open(points_file) as f:
        for line in f:
            if not line.strip():
                continue

            x, y = map(float, line.split())
            val = ((x - xc)**2) / (a*a) + ((y - yc)**2) / (b*b)

            if abs(val - 1) < eps:
                print(0)
            elif val < 1:
                print(1)
            else:
                print(2)

if __name__ == "__main__":
    main()
