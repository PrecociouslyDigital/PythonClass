class ExampleObject:
    def _init_(self, text):
        print("This method is run whenthe object is created")
        self.property = "This is a variable contained inside the object"
        self.text = text #This stores the text as another variable
    def printText(this):
        print(this.text)
    def ayyyyy(self):
        print("ayyyyy")
someObscureReference = ExampleObject("This is the text")
soomeObje.printText()