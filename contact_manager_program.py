#using a nested list
def display_menu():
   print('Contact Manager program')
   print('')
   print('COMMAN MENU')
   print('list - Display all contacts')
   print('view - View a contact')
   print('add - Add a contact')
   print('del - delete a contact')
   print('exit - Exit program')
print('')

def display(contact_list):
    if len(contact_list)== 0: #error checking code, there is no reason to loop trough an empty list
        print('There are no contacts in the list.\n')
        return
    else:
        i = 1
        for contact in contact_list:
            print(str(i) + '. '+ contact[0])
            i += 1
       

def view(contact_list):
    if len(contact_list)== 0: 
        print('There are no contacts in the list.\n')
        return
    
    else:
        number = int(input('Enter contact number: '))
        print('')
        i = number - 1
        for number in range(len(contact_list)):
           print('Name: '+ contact_list[i][0])
           print('Email: '+ contact_list[i][1])
           print('Phone: '+'+' + contact_list[i][2])
           break
                    
def add(contact_list):
    name = input('Name: ')
    email = input('Email: ')
    phone = input('Phone: ')
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contact_list.append(contact)
    print(contact[0] + ' was added.\n')

def delete(contact_list):
    number = int(input('Which number to delete: '))
    if number < 1 or number > len(contact_list):
        print('Invalid employee number\n')
    else:
        contact = contact_list.pop(number -1)
        print(contact[0] + ' was deleted')
           
def main():
    contact_list = [['Marilyn Monroe','marylyn@gmail.com', '1 235 687 5364'],
                    ['Abraham Lincoln','AbrahamLincoln@whitehouse.com', '11 33 4567 4587']]
    display_menu()
    while True:
        print('')
        command = input('Enter Command: ')
        print('')
        if command.lower() == 'list':
            display(contact_list)
        elif command.lower() == 'view':
            view(contact_list)
        elif command.lower() == 'add':
            add(contact_list)
        elif command.lower() == 'del':
            delete(contact_list)
        elif command.lower() == 'exit':
            break
        else:
            print('That is not a valid command. Please try again.\n')
    print('Bye')
    
    
    
if __name__=='__main__':
    main()