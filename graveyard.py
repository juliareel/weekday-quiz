

# Graveyard



# '''
# code type is either 'year' or 'month'
# '''
# def quizMonthYearCodes(codeType):
#     play = True
#     while play == True:
#         date = generateDate()
#         if codeType == 'year':
#             answer = calcYearCodeSimple(date.year)
#             # answer = calcYearCodeMod7(date.year)
#         elif codeType == 'month':
#             answer = MONTH_CODE_MAPPING.get(date.month)
#         else:
#             return "Unrecognized code type"
        
#         print(date)
#         while True:
#             response = input(f'Input the {codeType} code: ')
#             if int(response) == answer:
#                 print('Correct!')
#                 break
#             else:
#                 print('Incorrect, try again')
#         playagain = input('Again? Y or N: ').upper()
#         if playagain == 'N':
#             play = False

# '''
# stepType: can be either 'divby4floor' or 'mod7'
# range: [int, int] representing lower and upper bounds of possible values.
# ''' 
# def quizMathSteps(range, stepType):
#     lower_bound = range[0]
#     upper_bound = range[1]
#     play = True
#     while play == True:
#         val = random.randint(lower_bound, upper_bound)
#         if stepType == 'divby4floor':
#             answer = val // 4
#         elif stepType == 'mod7':
#             answer = val % 7
#         else:
#             return "Error: Unrecognized math step type."
#         print(val)
#         while True:
#             response = int(input('Answer: '))
#             if response == answer:
#                 print('Correct!')
#                 break
#             else:
#                 print('Incorrect, try again')
#         playagain = input('Again? Y or N: ').upper()
#         print('')
#         if playagain == 'N':
#             play = False

# def quizDayOfWeek():
#     play = True
#     while play == True:
#         date = generateDate()
#         answer_int = determineWeekday(date.month, date.day, date.year)
#         weekday_full = DAY_MAPPING.get(answer_int)
#         weekday_abr = DAY_MAPPING_ABBR.get(answer_int)
#         print(date)
#         while True:
#             response = input('Input the day of week: ').lower()
#             if response == weekday_full or response == weekday_abr:
#                 print('Correct!')
#                 break
#             else:
#                 print('Incorrect, try again')
#         playagain = input('Again? Y or N: ').upper()
#         print('')
#         if playagain == 'N':
#             play = False





# def quizDivBy4Floor(range=[48,99]):
#     play = True
#     while play == True:
#         val = random.randint(range[0], range[1])
#         print(val)
#         while True:
#             response = int(input('Input val divided by 4 (round down): '))
#             if response == val // 4:
#                 print('Correct!')
#                 break
#             else:
#                 print('Incorrect, try again')
#         playagain = input('Again? Y or N: ').upper()
#         print('')
#         if playagain == 'N':
#             play = False

# def quizMod7():
#     play = True
#     while play == True:
#         val = random.randint(1,160)
#         print(val)
#         while True:
#             response = int(input('Input val mod 7: '))
#             if response == val % 7:
#                 print('Correct!')
#                 break
#             else:
#                 print('Incorrect, try again')
#         playagain = input('Again? Y or N: ').upper()
#         print('')
#         if playagain == 'N':
#             play = False