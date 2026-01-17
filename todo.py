duties = []

while True:
    print('1-Add Task')
    print('2-List Task')
    print('3-Delete Task')
    print('4-Exit')

    userInput = int(input('Choose one of them(1-4): '))

    if userInput == 1:
        getText = input('Enter a duty: ')
        duties.append(getText)
        print('Duty Added Successfuly!\n')

    elif userInput == 2:
        if not duties:
            print('Please add a duty first!\n')
        else:
            for index,value in enumerate(duties):
                print(str(index + 1) + ': ' + value + '\n')

    elif userInput == 3:
        deleteInput = int(input('Enter a duty number to delete: '))
        duties.pop(deleteInput - 1)
        print('Duty deleted successfuly!\n') 

    elif userInput == 4:
        break
