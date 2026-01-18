import sqlite3
#import json

#try:
#    with open("duties.json", "r") as file:
#        duties = json.load(file)
#except:
#    duties = []

conn = sqlite3.connect("duties.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS duties(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    duty TEXT NOT NULL,
    done TEXT NOT NULL                     
)
""")

print('1-Add Task')
print('2-List Task')
print('3-Delete Task')
print("4-Mark Task Done")
print('5-Exit')

while True:
    try:
        userInput = int(input('Choose one of them(1-5): '))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if userInput == 1:
        getText = input('Enter a duty: ')
        #duties.append({'duty': getText, 'done': False})
        done = "Not Done"
        cursor.execute("INSERT INTO duties (duty, done) VALUES (?, ?)", (getText, done))
        conn.commit()

        print('Duty Added Successfuly!\n')

    elif userInput == 2:
        #if not duties:
        #    print('Please add a duty first!\n')
        #else:
        #    for index,value in enumerate(duties):
        #        if value["done"]:
        #            print(str(index + 1) + ': ' + value["duty"] + " - Done ✅\n")
        #        else:
        #            print(str(index + 1) + ': ' + value["duty"] + ' - Not Done \n')

        cursor.execute("SELECT id, duty, done FROM duties")
        duties = cursor.fetchall()

        if not duties:
            print("Please add a duty first!\n")
        else:
            for duty in duties:
                print(f"{duty[0]}: {duty[1]} - {duty[2]}\n")

    elif userInput == 3:
        try:
            deleteInput = int(input('Enter a duty number to delete: '))
            #duties.pop(deleteInput - 1)

            cursor.execute("DELETE FROM duties WHERE id = ?", (deleteInput,))
            conn.commit()

            print('Duty deleted successfuly!\n') 
        except:
            print("Please enter a valid number!\n")

    elif userInput == 4:
        try:
            markDoneInput = int(input("Enter the task number to mark as done: "))
            #duties[markDoneInput - 1]["done"] = True
            
            cursor.execute("UPDATE duties SET done = 'Done ✅' WHERE id = ?", (markDoneInput,))
            conn.commit()

            print("Task marked as done!\n")
        except:
            print("Please enter a valid number!\n")

    elif userInput == 5:
        #with open("duties.json", "w") as file:
        #    json.dump(duties, file)

        conn.close()
        print("Goodbye 👋")
        break
    else:
        print("Please choose a valid option!\n")
        
