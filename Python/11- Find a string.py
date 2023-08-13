def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):      # begins from 0 to len(string) - len(sub_string) + 1
        if string[i:i + len(sub_string)] == sub_string :    # in the first loop: if substring is exists in the range of 0 to total length - substring length then increment count
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)