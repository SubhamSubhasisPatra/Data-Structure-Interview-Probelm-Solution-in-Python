def show_name(counter=0, n=5):
    if counter > n:
        return
    print('SSP')
    show_name(counter + 1, n)


if __name__ == '__main__':
    show_name(1, 5)
