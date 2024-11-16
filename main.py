class Car:
    def __init__(self, model, mileage, year):
        self.model = model
        self.mileageOrg = mileage
        self.mileage = mileage * 2.35214583
        self.year = year
    def display(self):
        kindWordOld = ""
        kindWordIc = ""
        if self.year > 2018:
            kindWordIc = "and is iconic with car enthusiasts and lovers alike because of its modern and sleek feel"
            kindWordOld = " recently developed masterpiece"
        elif self.year > 1990:
            kindWordIc = "but is disliked by many due to its old components"
            kindWordOld = "n old and outdated car"
        else:
            kindWordIc = "and is enjoyed by antique-lovers because of its unique design"
            kindWordOld = "n antique car"
        
        
        print("The " + str(self.year) + " " + self.model + " is a" + kindWordOld + " that has " + str(self.mileageOrg) + " kmpl (" + str(self.mileage) + " mpg) " + kindWordIc + ".")

goodCar = Car("Ford Mustang", 4, 2023)
goodCar.display()
print("")
badCar = Car("Ford Oldstang", 4, 2000)
badCar.display()
print("")
oldCar = Car("Ford Antique", 4, 1973)
oldCar.display()