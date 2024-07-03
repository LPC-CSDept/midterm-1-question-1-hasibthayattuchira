

def main():
    number = []
    evencnt = 0
    even_count = 0
    even_group = False

    for i in range(10):
        number.append(int(input('Enter a number: ')))
        number.append(int)
        
    for num in number:
        if num % 2 == 0:
            even_count += 1
            if even_count == 2 and not even_group:
                evencnt += 1
                even_count = 0
                even_group = True
        else:
            even_count = 0
            even_group = False
                
        
        

    """
    ########################################
    Code Your Program here
    ########################################
    """
    print(evencnt)

    ########################################
    # Do not delete the return statement
    ########################################
    return evencnt


if __name__ == '__main__':
    main()
