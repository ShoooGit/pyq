def main():
    set_example_1 = {1, 2, 2, 3}
    print(set_example_1)

    list_example = [1, 1, 2, 3]
    set_example_2 = set(list_example)
    print(set_example_2)

    tuple_example = ('A', 'B', 'C', 'C')
    set_example_3 = set(tuple_example)
    print(set_example_3)

    empty_set = set()
    print(empty_set)


if __name__ == "__main__":
    main()