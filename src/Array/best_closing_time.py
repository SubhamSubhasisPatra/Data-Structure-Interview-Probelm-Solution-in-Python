def best_closing_time(customer):
    max_score = score = 0
    best_hour = - 1

    for i, c in enumerate(customer):
        score += 1 if c == 'Y' else -1

        if score > max_score:
            max_score, best_hour = score, i

    return best_hour + 1


if __name__ == '__main__':
    best_closing_time('YYNY')
    best_closing_time('NNNNN')
    best_closing_time('YYYY')
