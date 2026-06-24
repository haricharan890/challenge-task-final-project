# ==========================================
# FINAL CHALLENGE – ALL CONTROL FLOW CONCEPTS
# ==========================================


# ---------- INPUT VALIDATION ----------
def get_number(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = float(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Value must be >= {minimum}")
                continue

            if maximum is not None and value > maximum:
                print(f"Value must be <= {maximum}")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


# ---------- TEXT ADVENTURE GAME ----------
def text_adventure():
    print("\n=== TEXT ADVENTURE GAME ===")

    choice1 = input("Go to FOREST or CAVE? ").lower()

    if choice1 == "forest":
        choice2 = input("CLIMB tree or WALK deeper? ").lower()

        if choice2 == "climb":
            choice3 = input("LOOK around or REST? ").lower()

            if choice3 == "look":
                print("Ending 1: You found hidden treasure!")
            else:
                print("Ending 2: You slept and were rescued.")
        else:
            choice3 = input("FOLLOW river or RETURN? ").lower()

            if choice3 == "follow":
                print("Ending 3: You reached a peaceful village.")
            else:
                print("Ending 4: You safely returned home.")

    elif choice1 == "cave":
        choice2 = input("ENTER cave or RUN away? ").lower()

        if choice2 == "enter":
            choice3 = input("LIGHT torch or WALK in dark? ").lower()

            if choice3 == "light":
                print("Ending 5: You found ancient artifacts.")
            else:
                print("Ending 6: A monster chased you out.")
        else:
            print("Ending 7: You escaped safely.")

    else:
        print("Ending 8: You got lost.")


# ---------- TEMPERATURE CATEGORIZER ----------
def temperature_categorizer():
    print("\n=== TEMPERATURE CATEGORIZER ===")

    temp = get_number("Enter temperature: ")

    unit = input("C or F? ").upper()

    if unit not in ["C", "F"]:
        print("Invalid unit.")
        return

    # Convert F to C
    celsius = (temp - 32) * 5 / 9 if unit == "F" else temp

    if celsius < -20:
        category = "Extreme Cold"
    elif celsius < 0:
        category = "Very Cold"
    elif celsius < 10:
        category = "Cold"
    elif celsius < 20:
        category = "Cool"
    elif celsius < 30:
        category = "Pleasant"
    elif celsius < 40:
        category = "Warm"
    elif celsius < 50:
        category = "Hot"
    else:
        category = "Extreme Heat"

    print(f"Temperature = {celsius:.1f}°C")
    print("Category:", category)


# ---------- LEAP YEAR CALCULATOR ----------
def leap_year():
    print("\n=== LEAP YEAR CHECKER ===")

    year = int(get_number("Enter year: ", 1))

    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    result = "Leap Year" if is_leap else "Not a Leap Year"

    print(result)


# ---------- GRADE CALCULATOR ----------
def score_to_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"


def grade_calculator():
    print("\n=== GRADE CALCULATOR ===")

    scores = []

    subjects = ["Math", "Science", "English", "History"]

    for subject in subjects:
        score = get_number(f"{subject} score (0-100): ", 0, 100)
        scores.append(score)

    avg = sum(scores) / len(scores)

    all_passed = all(score >= 60 for score in scores)

    distinction = avg >= 85 and all_passed

    if distinction:
        result = "DISTINCTION"
    elif all_passed and avg >= 75:
        result = "FIRST CLASS"
    elif all_passed and avg >= 60:
        result = "SECOND CLASS"
    elif all_passed:
        result = "PASS"
    else:
        failed = sum(1 for score in scores if score < 60)
        result = f"FAIL ({failed} subjects failed)"

    overall_grade = score_to_grade(avg)

    print("\nAverage =", round(avg, 2))
    print("Highest =", max(scores))
    print("Lowest =", min(scores))
    print("Overall Grade =", overall_grade)
    print("Result =", result)


# ---------- MAIN MENU ----------
while True:
    print("\n========== DAY 3 FINAL CHALLENGE ==========")
    print("1. Text Adventure")
    print("2. Temperature Categorizer")
    print("3. Leap Year Checker")
    print("4. Grade Calculator")
    print("5. Exit")

    choice = input("Choose option: ")

    match choice:
        case "1":
            text_adventure()

        case "2":
            temperature_categorizer()

        case "3":
            leap_year()

        case "4":
            grade_calculator()

        case "5":
            print("Goodbye!")
            break

        case _:
            print("Invalid choice.")
