class Person:
    # initialize the constuctor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # create a method to introduce the a person
    def introduce( name, age, gender):
        return print("\nName is: ",name, "\nAge is: ", age, "\nGender is: ", gender)
    
# an instance of the class
p1 = Person
intro = p1.introduce("Hellen", 23, "female")
print(intro)