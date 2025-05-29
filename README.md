# 📆 Date Quiz Program

This is a command-line Python application that allows users to:
1. Take a quiz on various topics.
2. Manually calculate the weekday of a given date.
3. Exit the program.

---

## 🚀 Features

- **Quiz Mode**: Choose from multiple quiz types (e.g., mod 7 calculation, floor 4, year & month codes — defined in `QUIZ_TYPES`) and drill pieces of weekday calculation formula + full formula.
- **Date Calculation Mode**: Input any date (mm/dd/yyyy) and the app will tell you what day of the week it was.
- **User-Friendly CLI**: Interactive command-line prompts with input validation.

---

## 🧰 Requirements

Install required packages using:

```bash
pip install -r requirements.txt
```

---

## 🗂️ Project Structure

```
project/
├── app/
│   ├── quiz.py          # Quiz logic
│   ├── calcs.py         # Weekday calculation logic
│   └── globals.py       # Shared constants like QUIZ_TYPES and DAY_MAPPING
├── main.py              # Main program interface
├── requirements.txt     # Python dependencies
└── unittest.py          # (Assumed) unit tests
```

---

## 🧪 Running the App

To start the app, run:

```bash
python main.py
```

Follow the prompts:
- Enter `1` to take a quiz
- Enter `2` to calculate a weekday
- Enter `3` to exit

---

## 📅 Example Input (Date Calculation)

```plaintext
Enter choice (1-3): 2
Date to calculate (format mm/dd/yyyy): 07/04/2024
Day of week of 7/4/2024:
Thursday
```
