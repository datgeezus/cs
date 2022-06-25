def reformat(numbers):

    phones = []
    for _number in numbers:
        i = 0
        number = list(_number)
        prefix = number[i : i + 3]
        i = 4
        if number[i] != "-":
            prefix.append("-")
        area = number[i : i + 3]
        if number[i + 1] != "-":
            area.append("-")
        line = number[-4:]
        phones.append("".join(area + prefix + line))

    return phones


if __name__ == "__main__":
    print(reformat(["458-2227212", "458-222-7212", "4582227212"]))
