from app.globals import MONTH_CODE_MAPPING, CENTURY_CODE_MAPPING
'''
Accepts: Year as integer
Returns: year code mod 7
'''
def calcYearCode(year, simple=True):
    last2 = int(str(year)[-2:])
    floor4 = last2 // 4 
    yearCode = floor4 + last2 

    if simple==False: # checks if user prefers to mod 7 at this step, or keep it simple.
        return yearCode % 7
    
    return yearCode

''' 
Determines if a year is a leap year.
Accepts: Year as integer
Returns: Boolean - True if year is leap year, false if year is not a leap year
'''
def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

'''
Calculates the day of the week.
Accepts: A month, day, and year integer
Returns: the integer value representing the weekday
'''
def determineWeekday(month, day, year):
    centuryNum = int(str(year)[0:2])
    monthCode = MONTH_CODE_MAPPING.get(month, None)
    centuryCode = CENTURY_CODE_MAPPING.get(centuryNum, None)
    yearCode = calcYearCode(year)

    if monthCode is None:
        raise ValueError(f'No matching month code found for month {month}')
    if centuryCode is None:
        raise ValueError(f'No matching century code found for century {centuryNum}')

    add_codes = yearCode + centuryCode + monthCode + day

    # Adjust for Jan or Feb of a leap year:
    if isLeapYear(year) == True and (month == 1 or month == 2):
        add_codes -= 1
    
    result = add_codes % 7
    return result