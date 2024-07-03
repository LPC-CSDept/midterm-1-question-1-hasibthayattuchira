

def main():
    number = []
    evencnt = 0
    even_group = False

    for i in range(10):
        number.append(int(input('Enter a number: ')))
        number.append(int)
        
        for int in number:
            if number %2 == 0:
                evencnt += 1
                even_group = True
            else:
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
