if True:
  print "Since true is true, this will always print"
#--------------------#
test = 123

if test % 2 == 1:
  print "Your number is odd!"
else:
  print "Your number is even!"
#--------------------#
grade = "A"

if grade == "A":
  print "Great job!"
elif grade == "B":
  print "Not bad."
elif grade == "C":
  print ("Keep trying!")
else:
  print ("Work harder.")
#--------------------#
number = 125
print "Here is a number!"
if number >= 50:
  print "The number is above (or equal to) 50,"
  if number < 100:
    print " but it is less than 100!"
  elif number < 150:
    print " but it is less than 150!"
  else:
    print " and is really quite large!"
else:
  print "The number is less than 50!"
