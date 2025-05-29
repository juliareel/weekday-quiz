from app.calcs import calcYearCode, isLeapYear, determineWeekday
from main import acceptDateInput
from app.quiz import determine_correct_answers

def test_acceptDateInput():
    print(acceptDateInput())
# test_acceptDateInput()

#MANUAL
''' enter the following:
01/01/2020
11/11/2020
10/05/1967
09/30/1801
12/31/1999
'''
'''
def handle_day_of_week(prompt_data):
    answer_int = determineWeekday(prompt_data.month, prompt_data.day, prompt_data.year)
    full = DAY_MAPPING.get(answer_int)
    abr = DAY_MAPPING_ABBR.get(answer_int)
    return [full, abr]

def handle_year_code(prompt_data):
    return [str(calcYearCode(prompt_data.year))]

def handle_month_code(prompt_data):
    return [str(MONTH_CODE_MAPPING.get(prompt_data.month))]

def handle_century_code(prompt_data):
    return [str(CENTURY_CODE_MAPPING.get(prompt_data.month))]

def handle_mod7(prompt_data):
    return [str(prompt_data % 7)]

def handle_div_by_4_floor(prompt_data):
    return [str(prompt_data // 4)]
'''
def test_determine_weekday():
    assert determineWeekday(10, 12, 2022) == 3
    print('determine weekday: PASS')

QUIZ_TYPES = {  'Mod 7 Division': 'Modulo 7 of a random number',
                'Floor 4 Division': 'Integer division by 4',
                'Day of Week': 'Find the day of the week for a given date',
                'Year Code': 'Calculate the year code',
                'Month Code': 'Find the month code',
                'Century Code': 'Find the century code'
}

def test_handle_day_of_week():
    pass
 

def test_determine_correct_answers():
    # assert determine_correct_answers('Mod 7 Division', 
    pass

def test_calcYearCode():
    assert calcYearCode(1066) == 5
    assert calcYearCode(1879) == 0
    assert calcYearCode(1969) == 2
    assert calcYearCode(2000) == 0
    print('calcYearCode: PASS')

def test_isLeapYear():
    assert isLeapYear(1996) == True
    assert isLeapYear(2000) == True
    assert isLeapYear(2020) == True
    assert isLeapYear(2024) == True
    assert isLeapYear(1066) == False
    assert isLeapYear(1900) == False
    assert isLeapYear(1994) == False
    print('isLeapYear: PASS')

def test_determineWeekday():
    assert determineWeekday(8, 17, 1773) == 'Tuesday'
    assert determineWeekday(9, 3, 1814) == 'Saturday'
    assert determineWeekday(8, 15, 1968) == 'Thursday'
    assert determineWeekday(12, 10, 2013) == 'Tuesday'
    assert determineWeekday(12, 10, 2000) == 'Sunday'
    assert determineWeekday(1, 10, 2000) == 'Monday'
    assert determineWeekday(1, 10, 1900) == 'Wednesday'
    assert determineWeekday(9, 10, 1900) == 'Monday'
    assert determineWeekday(5, 12, 2098) == 'Monday'

    print('determineWeekday: PASS')

# def test_calcLeapYearAdjustment():
#     assert calcLeapYearAdjustment(2000, 1) == -1
#     assert calcLeapYearAdjustment(2000, 2) == -1
#     assert calcLeapYearAdjustment(2000, 3) == 0
#     assert calcLeapYearAdjustment(2001, 1) == 0
#     assert calcLeapYearAdjustment(2001, 5) == 0
#     assert calcLeapYearAdjustment(2004, 1) == -1
#     assert calcLeapYearAdjustment(2004, 2) == -1
#     print('calcLeapYearAdjustment: PASS')

def runTests():
    test_calcYearCode()
    test_isLeapYear()
    test_determineWeekday()
    # test_calcLeapYearAdjustment()

#runTests()
