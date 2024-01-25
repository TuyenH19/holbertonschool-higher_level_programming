#!/usr/bin/python3
def asc():
    result = ""
    for i in range(65, 91):
        if i % 2 == 0:
            result += chr(i + 32)
        else:
            result += chr(i)
    return (result)


result_string = asc()[::-1]
print(result_string)
