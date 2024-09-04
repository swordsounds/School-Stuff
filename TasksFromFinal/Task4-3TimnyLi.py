import pandas as pd

df = pd.read_csv("student_scores.csv")

if __name__ == "__main__":
    avg = df["Grades"].mean()
    print(f"The average grade is {round(avg, 2)}%")

    df = df[df["Grades"] > 80]
    print(f'Grades Above 80%: \n{df["Grades"]}')
