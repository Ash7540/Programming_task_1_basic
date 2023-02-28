def is_leap(year):
    lp = False

    # Write your logic here
    if (year % 100 == 0) and (year % 400 != 0):
        lp = False
    elif (year % 4 == 0):
        lp = True
    return lp
