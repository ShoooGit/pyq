def main():
    # 和集合を求めましょう
    union = {1, 2, 3} | {2, 3, 4}
    print(union)

    # 積集合を求めましょう
    intersection = {1, 2, 3} & {2, 3, 4}
    print(intersection)

    # 差集合を求めましょう
    difference = {1, 2, 3} - {2, 3, 4}
    print(difference)

    # 2つの集合の対称差
    sym_diff = {1, 2, 3} ^ {2, 3, 4}
    print(sym_diff)

    # 左辺の要素全てが右辺の集合に含まれている場合
    subset_1 = {1, 3} <= {1, 2, 3}
    print(subset_1)

    # 右辺の要素全てが左辺の集合に含まれている場合
    subset_2 = {4, 5, 6} >= {4, 5}
    print(subset_2)

    # 左辺に右辺の集合に存在しない要素が含まれている場合
    subset_3 = {3, 4} <= {1, 2, 3}
    print(subset_3)

if __name__ == '__main__':
    main()