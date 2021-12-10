# Ryan Lugo: RJL 12/9/21

def strings(string_one,string_two,string_three):

    sort = []

    first = list(string_one)
    sort += [(sorted(first,key=str.lower))]

    second = list(string_two)
    sort += [(sorted(second,key=str.lower))]

    third = list(string_three)
    sort += [(sorted(third,key=str.lower))]

    return sort

first_string = str(input("First string?: "))
second_string = str(input("Second string?: "))
third_string = str(input("Third string?: "))

print(strings(first_string,second_string,third_string))