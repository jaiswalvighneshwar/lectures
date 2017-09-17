marks = float(raw_input("Enter marks: "))
if marks >100 or marks <0:
    print str(marks) , " is invalid"
elif marks >= 40:
    print "C"
elif marks >= 60:
    print "B"
elif marks >=70 :
      print "a"
else :
    print "Fail"
