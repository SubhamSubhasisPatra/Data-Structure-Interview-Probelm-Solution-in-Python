"""

Input Format: N = 5

Result:
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Explanation: There are 5 rows in the output matrix. Each row corresponds to each one of the rows in the image shown above.

"""


def optimize_solution(N):
    r = [[1] * (i + 1) for i in range(N)]
    for i in range(N):
        for j in range(1, i):
            r[i][j] = r[i - 1][j - 1] + r[i - 1][j]
    print(r)


def show_triangles(N):
    result = []

    for i in range(N):
        if i == 0:
            result.append([1])
        elif i == 1:
            result.append([1, 1])
        else:
            # The logic
            element = result[-1]
            first, last = element[0], element[-1]
            tempArray = []
            for j in range(0, len(element) - 1):
                total = element[j] + element[j + 1]
                tempArray.append(total)
            result.append([first, *tempArray, last])
    print(result)


if __name__ == '__main__':
    N = 5
    show_triangles(N)
    N = 6
    optimize_solution(N)
