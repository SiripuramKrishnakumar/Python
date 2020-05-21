def div(a, b):
    print(a - b)


def decFun(func):
    def inner(a, b):
        if a < b:
            a, b = b, a

        return func(a, b)

    return inner


div = decFun(div)

div(1, 4)

print(__name__)


def main():
    print('its prints only when i run this file not in modules function due to below condition')


if __name__ == "__main__":
    main()
