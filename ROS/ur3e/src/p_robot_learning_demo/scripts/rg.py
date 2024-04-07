import argparse


def func1(x):
    print('func3', x)


def func2(x):
    print('func3', x)


def func3(x):
    print('func3', x)


if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="")
    parse.add_argument("--num_layers", type=int, required=True, help="Network depth.")
    while True:
        args = parse.parse_args()
        print(args.num_layers)