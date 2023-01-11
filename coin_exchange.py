# coin exchange
import math


def main():
    money = 21
    coins = [25, 5, 1]

    q_change = 0
    n_change = 0
    p_change = 0
    qd = money / 11
    if qd > 1:
        q_change = math.floor(abs(qd))
        money -= q_change * 11

    nd = money / 3
    print(money, nd)
    if nd > 1:
        n_change = math.floor(abs(nd))
        money -= n_change*3

    p_change = money

    print("Exchange would be: ", q_change, n_change, p_change)


if __name__ == "__main__":
    main()
