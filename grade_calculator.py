# grade_calculator.py — Uses all control flow concepts


def get_score(subject_name):
    """Get a valid score (0-100) from user."""
    while True:
        try:
            score = float(input(f"Enter {subject_name} score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a number.")


def score_to_grade(score):
    """Convert score to grade using if/elif chain."""
    if score >= 90:
        return "A+", "Outstanding"
    elif score >= 85:
        return "A", "Excellent"
    elif score >= 80:
        return "B+", "Very Good"
    elif score >= 75:
        return "B", "Good"
    elif score >= 70:
        return "C+", "Above Average"
    elif score >= 65:
        return "C", "Average"
    elif score >= 60:
        return "D", "Below Average"
    else:
        return "F", "Fail"


def analyze_performance(scores):
    """Analyze overall performance."""
    avg = sum(scores) / len(scores)
    min_score = min(scores)
    max_score = max(scores)

    # Check whether all subjects are passed
    all_passed = all(s >= 60 for s in scores)

    # Distinction condition
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
        failed_count = sum(1 for s in scores if s < 60)
        result = f"FAIL ({failed_count} subject(s) failed)"

    return avg, min_score, max_score, result


# ================= MAIN PROGRAM =================

subjects = ["Mathematics", "Science", "English", "History"]
scores = []

print("=== Student Grade Calculator ===\n")

# Input scores and display individual grades
for subject in subjects:
    score = get_score(subject)
    scores.append(score)

    grade, label = score_to_grade(score)
    print(f"→ {subject}: {grade} ({label})\n")

# Analyze overall performance
avg, low, high, result = analyze_performance(scores)

# Overall grade based on average
overall_grade, overall_label = score_to_grade(avg)

# Display report
print("=" * 40)
print("STUDENT REPORT")
print("=" * 40)

print(f"Average Score : {avg:.1f}/100")
print(f"Highest Score : {high}")
print(f"Lowest Score  : {low}")
print(f"Overall Grade : {overall_grade} ({overall_label})")
print(f"Result        : {result}")

print("=" * 40)
