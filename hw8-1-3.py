# Ryan Lugo: RJL 12/9/21


def string_halfing(string1,stringHalf):

    string_value = "nope"
    string_value2 = "well"

    string_value = ("First half of the string", string1[0:stringHalf])
    string_value2 = ("Second half of the string", string1[stringHalf:len(string1)])

    return string_value,string_value2

the_string = str(input("What word do you want to be split in half?: " ))
string_halfed = len(the_string) // 2

print(string_halfing(the_string,string_halfed))