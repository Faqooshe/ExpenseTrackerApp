'''


from datetime import datetime





def inputEx():
    inputs = input('Enter name: ')
    timestamp = datetime.now().strftime("%Y/%m/%d %H:%M")

    note = f"[{timestamp}] : {inputs}"



    with open("Trackname.txt", 'a') as file:
            file.write(note + '\n')
    

    with open("Trackname.txt", 'r') as file:
        for line in file:
            print(line)





def ShowInputs():
     input1 = input('Start date: ')
     input2 = input('End date: ')

     startdate = datetime.strptime(input1, "%Y/%m/%d")
     enddate = datetime.strptime(input2, "%Y/%m/%d")

     with open("Trackname.txt", 'r') as file:
          for line in file:
               if line.startswith('['):
                    date_str = line[1:17]
                    date_note = datetime.strptime(date_str, "%Y/%m/%d %H:%M")

                    if startdate <= date_note <= enddate:
                         date_part = date_note.strftime("%Y/%m/%d")
                         note_text = line[18:]

                         print(date_part, note_text)
          

ShowInputs()

'''
from datetime import datetime
import os

class ExpenseTracker:
    def __init__(self):
        self.expense_Tracker = {}
        
    def addExpense(self):
        while True:
            print('Add an expense.\n')
            datestump = datetime.now().strftime("%Y-%m-%d %H:%M")

            while True:
                try:
                    itemName = input('Enter the Item name: ')
                    if itemName == '':
                        raise ValueError('It mus not be Empty!')
                    elif not itemName.isalpha():
                        raise ValueError('Write only letters.')
                    break
                except ValueError as e:
                    print('Error: ', e)


            while True:
                try: 
                    itemCategory = input('Enter the Item Category: ')
                    if itemCategory == '':
                        raise ValueError('It mus not be Empty!')
                    elif not itemCategory.isalpha():
                        raise ValueError('Write only letters.')
                    break
                except ValueError as e:
                    print('Error: ', e)

            while True:
                try:
                    itemExpense = int(input('Enter the Price: '))
                except ValueError:
                    print('Please enter a number.')

                with open('ExpenseList.txt', 'a') as file:
                        line = f"{datestump} | {itemName} | {itemCategory} | {itemExpense} \n"
                        file.write(line)
                

                        print('\nFile saved')
                        print(f"{datestump} - {itemName} ({itemCategory}) : {itemExpense}\n")
                
                break

            exitOption = input('Exit the Option (yes/no): ').lower()
            if exitOption == 'yes':
                print('GoodBye')
                break
        
    def searchExpense(self):
        while True:
            found = False
            S_itemName = input('Enter the item name: ').lower()

            try:
                with open('ExpenseList.txt', 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        parts = line.strip().split('|')
                        if len(parts) == 4:
                            date, item, cat, amount = parts
                            if item.strip().lower() == S_itemName:
                                print(f"{item} ':' {amount}")
                                found = True
                if not found:
                    print("Item doesn't exist")
            except FileNotFoundError:
                print('No notes found!')

            exitOption = input('Exit the Option (yes/no): ').lower()
            if exitOption == 'yes':
                print('GoodBye')
                break
                            
    def deleteExpense(self):
        while True:
            deleteItem = input('Enter item name: ')
            found = False

            try:
                with open('ExpenseList.txt', 'r') as file:
                    lines = file.readlines()

                with open('ExpenseList.txt', 'w') as file:
                        for line in lines:
                            parts = line.strip().split('|')
                            if len(parts) == 4:
                                date, item, cat, amount = parts
                                if item.strip().lower() == deleteItem.lower():
                                    print('Item is deleted.')
                                    found = True
                                    continue
                                file.write(line)

                if not found:
                    print('Item not in the note.')

            except FileNotFoundError:
                print('No notes are available.')

            exitOption = input('Exit the Option (yes/no): ').lower()
            if exitOption == 'yes':
                print('GoodBye')
                break

    def viewAllExpenses(self):
        while True:
            print('Monthly')
            print('Yearly')
            print('Custom')

            Showoption = (input('Choose option: '))
            if Showoption == '1':
                self.monthlyExpense()
            if Showoption == '2':
                self.YearlyExpense()
            if Showoption == '3':
                self.CustomExpense()
             
          #  print('All your expenses.')
            #with open('ExpenseList.txt', 'r') as file:
              #  for AllLines in file:
                    #print(AllLines)
           # exitOption = input('Exit the Option (yes/no): ').lower()
           # if exitOption == 'yes':
               # print('GoodBye')
               # break

    def totalAamountSpent(self):
        while True:
            with open('ExpenseList.txt', 'r') as file:
                total = 0
                try:
                    for line in file:
                        parts = line.strip().split('|')
                        if len(parts) == 4:
                            date, item, cat, amount = parts
                            total += float(amount.strip())
                    print('Your total Expense is: ', total)
                except FileNotFoundError:
                    print('No notes found')
                
            exitOption = input('Exit the Option (yes/no): ').lower()
            if exitOption == 'yes':
                print('GoodBye')
                break

    def filterByCategory(self):
        while True:
            found = False
            try:
                category = input('Enter Category: ')
                if category == '':
                    raise ValueError('This cannot be Empty!')
                elif not category.isalpha():
                    raise ValueError('Please, Enter letters only.')
            except ValueError as e:
                print('Error: ', e)
                continue

            with open('ExpenseList.txt', 'r') as file:
                try:
                    for lines in file:
                        parts = lines.strip().split('|')
                        if len(parts) == 4:
                            date, item, cat, amount = parts
                            if cat.strip().lower() == category.lower():
                                    print(f"{cat}: {item}({amount})")
                                    found = True
                    if not found:
                        raise ValueError("This category doesn't exist.")
                except ValueError as e:
                     print('Error: ', e)

            exitOption = input('Exit the Option (yes/no): ').lower()
            if exitOption == 'yes':
                print('GoodBye')
                break

    def exitProgram(self):
            exitOption = input('Wanna exit the Program (yes/no): ').lower()
            if exitOption == 'yes':
                print('GoodBye')
                exit()

    def monthlyExpense(self):
        while True:
            print('\nMonthly Expense.')
            
            
            found = False
            while True:
                try:
                    yearName = input('Enter the Year:').strip()
                    if yearName == '':
                        raise ValueError('It must not be empty!')
                    if not yearName.isdigit():
                        raise ValueError('It must be a number!')
                    if not len(yearName) == 4:
                        raise ValueError('It must not be more/less than 4 digits.')
                    realyear = int(yearName)
                    break
                except ValueError as e:
                    print('error: ', e)

            while True:
                try:
                    monthName = input('Enter month name: ').strip()
                    if monthName == '':
                            raise ValueError('It must not be empty!')
                    if not monthName.isdigit():
                            raise ValueError('It must be a number!')
                    if not (1 <= int(monthName) <= 12):
                        raise ValueError('It must be between 1-12')
                    realmonth = int(monthName)
                    break
                except ValueError as e:
                        print('error: ', e)
                        
            while True:
                try:
                    with open('ExpenseList.txt', 'r') as file:
                        for line in file:
                            parts = line.strip().split('|')
                            if len(parts) == 4:
                                date_str = parts[0].strip()

                                realDate = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                                if realDate.year == realyear and realDate.month == realmonth:
                                    print(f"{realDate.strftime('%Y-%m-%d')} - {parts[1]} ({parts[2]} : {parts[3]})")
                                    found = True
                                    
                    if not found:
                        print('No expenses found in ', realyear, realmonth)  
                    break
                except ValueError:
                    print('No expense file found!')  

    def YearlyExpense(self):
        while True:
            found = False
            while True:
                print()
                try:
                    yearInput = input('Enter the year: ').strip()
                    if yearInput == '':
                        raise ValueError('It must not be Empty!')
                    if not yearInput.isdigit():
                        raise ValueError('It must be a number!')
                    if not len(yearInput) == 4:
                        raise ValueError('It must be 4 digits!')
                    realYear = int(yearInput)
                    break
                except ValueError as e:
                    print('Error: ', e)
                
            while True:
                try:
                    with open('ExpenseList.txt', 'r') as file:
                        for line in file:
                            parts = line.strip().split('|')
                            if len(parts) == 4:
                                dateStr = parts[0].strip()
                                realDate = datetime.strptime(dateStr, "%Y-%m-%d %H:%M")
                                
                                if realDate.year == realYear:
                                    print(f"{realDate.strftime('%Y-%m-%d')} - {parts[1]}{parts[2]} : {parts[3]}")
                                    found = True
                    if not found:
                        raise('No items found in that year,', realYear)
                    break
                except FileNotFoundError:
                    print('No files found')


    def CustomExpense(self):
        while True:
            try: 
                stardate_str = input('Enter the start date (YYYY-MM-DD): ')
                enddate_str = input('Enter the end date (YYYY-MM-DD): ')
                if stardate_str or enddate_str == '':
                    raise ValueError('It must not br empty!')
            except ValueError as e:
                print("❌ Invalid date format. Use YYYY-MM-DD.")

            #From string to date
            startDate = datetime.strptime(stardate_str, "%Y-%m-%d").date()
            EndDate = datetime.strptime(enddate_str, "%Y-%m-%d").date()

            with open('ExpenseList.txt', 'r') as file:
                for line in file:
                    parts= line.strip().split('|')
                    if len(parts) == 4:
                        date_str = parts[0].strip()
                        date_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M").date()
                        if startDate <= date_date <= EndDate:
                            date_prt = date_date.strftime("%Y-%m-%d")
                            print(f"{date_prt} - {parts[1]} ({parts[2]} : {parts[3]})")

            exitOption = input('Exit the Option (yes/no): ').lower()
            if exitOption == 'yes':
                print('GoodBye')
                break




def mainMenu():
    system = ExpenseTracker()
    while True:
        print('1: Add Expense')
        print('2: Search Expense')
        print('3: Delete Expense')
        print('4: View All Expense')
        print('5: Total Amount Spent')
        print('6: Filter by category')
        print('7: Eixt the Program')

        option = input('\nChoose option (1-7): \n')
        if option == '1':
            system.addExpense()
        elif option == '2':
            system.searchExpense()
        elif option == '3':
            system.deleteExpense()
        elif option == '4':
            system.viewAllExpenses()
        elif option == '5':
            system.totalAamountSpent()
        elif option == '6':
            system.filterByCategory()
        elif option == '7':
            system.exitProgram()


mainMenu()


