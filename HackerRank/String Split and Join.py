def split_and_join(line):
    # write your code here
    # Split the input string on space delimiter
    words = line.split(" ")
    
    # Join the words using hyphen
    result = "-".join(words)
    
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
