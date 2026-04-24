import pandas as pd


def check_data_issues(df):
    issues = []

    # Missing values
    missing = df.isnull().sum()
    for col, val in missing.items():
        if val > 0:
            issues.append(f"Column '{col}' has {val} missing values")

    # Duplicates
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        issues.append(f"Dataset has {duplicates} duplicate rows")

    return issues


def generate_suggestion(issue):
    if "missing values" in issue:
        return "Consider handling missing values using imputation (mean/median) or removing affected rows."

    elif "duplicate" in issue:
        return "Consider removing duplicate rows using deduplication techniques."

    else:
        return "Review and clean the dataset."


def main():
    df = pd.read_csv("sample_data.csv")

    print("\nChecking data...\n")

    issues = check_data_issues(df)

    if not issues:
        print("No data issues found ✅")
        return

    for issue in issues:
        print(f"\nIssue: {issue}")

        suggestion = generate_suggestion(issue)
        print(f"AI Suggestion: {suggestion}")


if __name__ == "__main__":
    main()