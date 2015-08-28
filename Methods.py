print "It's over " + "9000"
print "It's over " + "the rainbow"
print "It's over " + "between us"

repeat = "It's over"
print repeat + "9000"
print repeat + "the rainbow"
print repeat + "between us"

def itsOver(whatsOver):
    print "It's over " + whatsOver

itsOver("9000")
itsOver("the rainbow")
itsOver("between us")

def betterItsOver(whatsOver):
    return "It's over " + whatsOver

print "See, " + betterItsOver("9000")

lineOfText = raw_input("This is the prompt")