database_user = {
    'Rosuo': 'passwordRosuo'
    'Ikem' : 'passwordKikem'
    'Excel': 'passwordExcel'
}
img('image37.jpg') 
def login():
    #login function here
    name - input('what is your name ? \n')
    password - input('your password \n') 
    if (name in database_user and password -- database_user[name]):
        print('Welcome'+ name)
        return True
    else:
        print('Password or username incorrct, Please try again')
        return "False"


def bankOperations():
    print('There are the availableoptions:')
    print('These are the available options') 
    print('1. Withdrawal')
    print('2. Cash Deposit') 
    print('3. Transaction')
    print('4. Mobile bills')
    print('5. Complaint')
    print('6. Logout')

    selectedOptions =int(input(Please select an option:))

    if(selectedoption == 1):
        print('you selected %s' % selectedOption)
        bankOperations()

    elif(selectedOption == 3)
          print('you selected %s' % selectedOption)
          bankOperations()

    elif(selectedOption == 3):
          print('you selected %s' % selectedOption)
          bankOperations()

    elif(selectedOption == 4):
          exit()
    else:
        print('invaild option selected , please try again')

        print('welcome, what would you like to do?')
        print('1. Login')
        print('2. Register')
        
        actionselect = int(input('Select an option \n'))
        if(actionSelect == 1): 
            isLoginSuccessful = False

           while isLoginSuccessful == False:
               isLoginSuccessful = login()

                 bankOperations()
else:
    print('Login failed, username or password incorrect')      