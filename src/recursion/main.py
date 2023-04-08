counter = 0


def show():
    global counter
    if counter == 3:
        return
    print(counter)
    counter += 1
    show()


if __name__ == '__main__':
    show()
