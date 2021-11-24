def show_args(arg1, arg2, arg3="THREE"):
    print(arg1, arg2, arg3)


if __name__ == '__main__':
    some_args = range(3)
    more_args = {
        "arg1": "ONE",
        "arg2": "TWO"
    }

    print("Unpacking a sequence.", end=" ")
    show_args(*some_args)

    print("Unpacking a dictionary.", end=" ")
    show_args(**more_args)
