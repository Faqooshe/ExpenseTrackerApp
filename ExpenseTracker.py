
class ExpenseTracker:
    def __init__(self):
        self.expense_Tracker = {}
        
    def addExpense(self):
        while True:
            print('Add an expense.\n')

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

                #self.expense_Tracker[itemName] = {'Category': itemCategory, 'Price': int(itemExpense)}

                with open('ExpenseList.txt', 'a') as file:
                    #for item, details in self.expense_Tracker.items():
                        #line = f"{item} | {details['Category']} | {details['Price']} \n"
                        line = f"{itemName} | {itemCategory} | {itemExpense} \n"
                        file.write(line)
                

                        print('\nFile saved')
                        print(f"{itemName} ({itemCategory}) : {itemExpense}\n")
                
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
                        if len(parts) == 3:
                            item, cat, amount = parts
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
                            if len(parts) == 3:
                                item, cat, amount = parts
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
            print('All your expenses.')
            with open('ExpenseList.txt', 'r') as file:
                for AllLines in file:
                    print(AllLines)
            exitOption = input('Exit the Option (yes/no): ').lower()
            if exitOption == 'yes':
                print('GoodBye')
                break

    def totalAamountSpent(self):
        while True:
            with open('ExpenseList.txt', 'r') as file:
                total = 0
                try:
                    for line in file:
                        parts = line.strip().split('|')
                        if len(parts) == 3:
                            item, cat, amount = parts
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
                        if len(parts) == 3:
                            item, cat, amount = parts
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




