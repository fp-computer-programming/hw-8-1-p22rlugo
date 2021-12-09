# Ryan Lugo: RJL 12/9/21

def strings():
    first_string = str(input("First string?: "))
    second_string = str(input("Second string?: "))
    third_string = str(input("Third string?: "))

    sort = []

    first = list(first_string)
    sort += [(sorted(first,key=str.lower))]

    second = list(second_string)
    sort += [(sorted(second,key=str.lower))]

    third = list(third_string)
    sort += [(sorted(third,key=str.lower))]

    return sort

print(strings())