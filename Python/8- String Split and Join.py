def split_and_join(line):
    line = line.split(" ")          # ['this', 'is', 'a', 'string']
    return "-".join(line)           # this-is-a-string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)