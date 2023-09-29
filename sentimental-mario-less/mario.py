# TODO
def main():
    height = get_height()

    for i in range(height):
        for j in range(height, i + 1, -1):
            print(" ", end="")
        print("#" * (i + 1))


def get_height():
    height = input("Height: ")

    while height.isnumeric() != True or int(height) > 8 or int(height) < 1:
        height = input("Height: ")

    height = int(height)
    return height


main()