""""

   5
  /
 4
/
3
\
 2
  \
   1

""""

def rev_display(N):
    if N < 1:
        return
    print(N)
    rev_display(N - 1)


if __name__ == '__main__':
    rev_display(5)
