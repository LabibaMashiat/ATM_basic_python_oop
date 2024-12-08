class Atm:
    # Constructor
    #special/magic/dunder methods
    #In class all are methods ,not function
    #Constructor will execute at the of object creating.Object does not call it.
    #Constructor is used when app is initially opened
    #Constructor is used when control can not be given to user
    #self is a object.If it is an object then it stored to somewhere
    #self is nothing but currently processing object
    #class has only two things. 1) Data and 2) Method. 
    #These two can be accessed by the objects of that class only.
    #In a same class one method can not directly access another method
    #For this we use self which is an object
    __count=1
    def __init__(self):
        self.pin=""
        self.balance=0
        self.sno=Atm.__count
        Atm.__count+=1
        #print("Memory address of the object:", id(self))
        self.menu()
    @staticmethod
    def get_count():
        return Atm.__count
    @staticmethod
    def set_count(new_pin):
        if type(new_pin)==int:
            Atm.__count=new_pin
        else:
            print("Not Allowed")
        
        
    def menu(self):
        while True:
            user_input=input("""Hello! How Would You Like To Proceed:
                 1)Enter 1 to create pin.
                 2)Enter 2 to deposit.
                 3)Enter 3 to withdraw
                 4)Enter 4 to check balance
                 5)Enter 5 to exit.
              """)
            if user_input=="1":
                self.create_pin()
            elif user_input=="2":
                self.deposit_amount()
            elif user_input=="3":
                self.withdraw_amount()
            elif user_input=="4":
                self.check_balance()
               
            else:
                print("Bye")
                break
    
    def create_pin(self):
        self.pin=input("Create your pin = ")
        print("Pin Create successfully.")

    def deposit_amount(self):

        temp=input("Enter your pin = ")
        if temp==self.pin:
            amount=int(input("Enter the amount of deposit= "))
            self.balance=self.balance+amount
            print("Deposit successfully.")
        else:
            print("Invalid Pin")
    def withdraw_amount(self):
        temp=input("Enter your pin")
        if temp==self.pin:
            amount=int(input("Enter the amount of withdraw= "))
            if amount<self.balance:
                self.balance=self.balance-amount
                print("Withdraw Successful")
            else:
                print("Your balance has not sufficient amount to withdraw")
        else:
            print("Invalid Pin.")
    def check_balance(self):
        print("Your current balance is= ",self.balance)