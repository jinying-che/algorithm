def insert_sort(arr):
    if len(arr) <= 1:
        return arr
    for i, item in enumerate(arr):
        print(f"{i} -> {item}")


if __name__ == '__main__':
    insert_sort([3, 2, 1])
