print ("It's over " + "9000")
print ("It's over " + "the rainbow")
print ("It's over " + "between us")
#--------------------#
repeat = "It's over"
print (repeat + "9000")
print (repeat + "the rainbow")
print (repeat + "between us")
#--------------------#
def itsOver(whatsOver):
    print ("It's over " + whatsOver)

itsOver("9000")
itsOver("the rainbow")
itsOver("between us")
#--------------------#
def makeTwentyPercentCooler(percentage):
    return "it's " + str(percentage * 1.2) + "% cool"

print "If you take 100% cool and make it twenty percent cooler," + makeTwentyPercentCooler(100)
#--------------------#
def basicMath(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Error: Invalid operator"

print "The answer to 3 + 4 is" + str(basicMath(3, "+", 4)
print "The answer to 3 - 4 is" + str(basicMath(3, "-", 4)
print "The answer to 3 * 4 is" + str(basicMath(3, "*", 4)
print "The answer to 3 / 4 is" + str(basicMath(3, "/", 4)
print "The answer to 3 # 4 is" + str(basicMath(3, "#", 4)
#--------------------#
name = input("Greetings, USER. What is your name?")
print "Hello, " + name + "."
