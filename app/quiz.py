import datetime, random
from app.calcs import calcYearCode, determineWeekday
from app.globals import MONTH_CODE_MAPPING, DAY_MAPPING_ABBR, DAY_MAPPING, CENTURY_CODE_MAPPING, QUIZ_INPUT_TYPE

'''
Generates a random date.
Accepts: Optional start and end date parameters. 
If no start/end date given, uses 1/1/1753 through 12/31/2300
Returns: Date, DT object
'''
def generateDate(start=datetime.date(1753, 1, 1), end=datetime.date(2300, 12, 31)):
    num_days = (end - start).days
    rand_days = random.randint(1, num_days)
    random_date = start + datetime.timedelta(days=rand_days)
    return(random_date)

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

dispatch = {
    'Day of Week': handle_day_of_week,
    'Year Code': handle_year_code,
    'Month Code': handle_month_code,
    'Century Code': handle_century_code,
    'Mod 7 Division': handle_mod7,
    'Floor 4 Division': handle_div_by_4_floor
}

def determine_correct_answers(quiz_type, prompt_data):
    handler = dispatch.get(quiz_type)
    if not handler:
        raise ValueError(f'Unrecognized quiz type: {quiz_type}')
    return handler(prompt_data)


def play_quiz(quiz_type, val_range=[1,160]):
    play = True
    while play == True:
        input_type =  QUIZ_INPUT_TYPE.get(quiz_type)
        if not input_type:
            raise ValueError(f'Unrecognized quiz type: {quiz_type}')
        
        if input_type == 'int':
            prompt_data = random.randint(val_range[0], val_range[1])
            print(f'Value to calculate: {prompt_data}')
        elif input_type == 'date':
            prompt_data = generateDate()            
            print(f'Date to calculate: {prompt_data.strftime("%B")} {prompt_data.day}, {prompt_data.year}')
        
        valid_answers = determine_correct_answers(quiz_type, prompt_data)
        while True:
            response = input('Answer: ').lower()
            save_answers = valid_answers
            save_response = response
            if response in valid_answers:
                print('Correct!')
                break
            else:
                print('Incorrect, try again')
        play_again = input('Again? Y or N: ').upper()
        print('')
        if play_again == 'N':
            play = False

 