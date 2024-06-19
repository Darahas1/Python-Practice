
year = int (input ("Enter any year that is to be checked for leap year: "))

if (year % 4) == 0:

    if (year % 100) == 0:

        if (year % 400) == 0:
            print ("The given year is a leap year")

        else:
            print ("It is not a leap year")

    else:
        print ("It is not a leap year")

else:     
    print ("It is not a leap year")