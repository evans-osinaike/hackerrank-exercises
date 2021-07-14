class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = initialAge
        if self.initialAge < 0:
            print('Age is not valid, setting age to 0.')

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.initialAge < 13:
            print('You are young.')
        elif self.initialAge < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

    def yearPasses(self):
        # Increment the age of the person in here
        self.initialAge += 1

t = int(input('Input the number of instances you want to test the class over: '))
for i in range(0, t):
    age = int(input('How old is the person?: '))         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("------------------------------")