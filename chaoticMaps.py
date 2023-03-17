def logistic(u, x):
    return x * u * (1 - x)


def tent(r, x):
    if x < 0.50000:
        return r * x
    else:
        return r * (1 - x)


def fog(u, r, x):
    if x < 0.5000:
        return u * r * x * (1 - r * x)
    else:
        return u * r * (1 - x) * (1 - r * (1 - x))


def deriv_logistic(u, x):
    return u * (1 - 2 * x)

