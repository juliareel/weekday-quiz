from app.quiz import play_quiz
from app.calcs import determineWeekday
from app.globals import DAY_MAPPING, QUIZ_TYPES

def list_main_options():
    print("\nChoose a mode:")
    print("1. Take a quiz")
    print("2. Manually determine weekday, you input date")
    print("3. Exit\n")

def list_quiz_options():
    print("Choose a quiz type:\n")
    for i, (key, desc) in enumerate(QUIZ_TYPES.items(), start=1):
        print(f"{i}. {key} – {desc}")
    print()

def get_quiz_type():
    quiz_keys = list(QUIZ_TYPES.keys())
    while True:
        choice = input("Enter quiz number or name: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(quiz_keys):
                return quiz_keys[idx]
        elif choice in quiz_keys:
            return choice
        print("Invalid choice. Please try again.\n")

def accept_date_input():
    date_str = input('Date to calculate (format mm/dd/yyyy): ')
    try:
        month = int(date_str[0:2])
        day = int(date_str[3:5])
        year = int(date_str[6:10])
        return month, day, year
    except (ValueError, IndexError):
        print("Invalid format. Please use mm/dd/yyyy.")
        return accept_date_input()

def handle_manual_date_calc():
    print("\nWeekday Calculation Mode")

    month, day, year = accept_date_input()
    weekday_val = determineWeekday(month, day, year)
    weekday = DAY_MAPPING.get(weekday_val)
    
    print(f"\nDay of week of {month}/{day}/{year}:")
    print(f"{weekday.capitalize()}")
    print()
    input("Press Enter to return to the main menu...")
    return 

def main():
    print("\n📅 Welcome to the Date Quiz Program!")
    
    while True:
        list_main_options()
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            list_quiz_options()
            quiz_type = get_quiz_type()
            print(f"\nYou selected: {quiz_type}\n")
            play_quiz(quiz_type)
        
        elif choice == '2':
            handle_manual_date_calc()
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == '__main__':
    main()
