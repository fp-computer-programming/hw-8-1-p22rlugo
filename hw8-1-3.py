# Ryan Lugo: RJL 12/9/21


def string_halfing():
    the_string = str(input("What word do you want to be split in half?: " ))
    string_halfed = len(the_string) // 2

    string_value = "nope"
    string_value2 = "well"

    string_value = ("First half of the string", the_string[0:string_halfed])
    string_value2 = ("Second half of the string", the_string[string_halfed:len(the_string)])

    return string_value,string_value2

print(string_halfing())