def nb_year(p0, percent, aug, p):
    initial = []
    num = 0
    per = percent/100
    n = p0 + p0 * per + aug
    while n <= p:
        if n <= p:
            num += n
            initial.append(num)
            continue
        else:
            break

    return initial

print(nb_year(1000, 2, 50, 1345))