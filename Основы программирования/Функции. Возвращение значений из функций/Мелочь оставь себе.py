def take_large_banknotes(banknotes):
    mony = []
    for i in banknotes:
        if i > 10:
            mony.append(i)

    return mony
