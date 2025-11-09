
import pandas as pd


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Salary': [45000, 54000, 50000, 62000, 47000]
}

df = pd.DataFrame(data)
print("Employee DataFrame:\n", df)

# a. Print first five rows
print("\nFirst Five Rows:\n", df.head())

# b. Summary statistics for Age and Salary
print("\nSummary Statistics:\n", df[['Age', 'Salary']].describe())

# c. Average salary in HR department
avg_hr_salary = df[df['Department'] == 'HR']['Salary'].mean()
print("\nAverage Salary (HR Dept):", avg_hr_salary)

df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame with Bonus:\n", df)


filtered_df = df[(df['Age'] >= 25) & (df['Age'] <= 30)]
print("\nEmployees aged between 25 and 30:\n", filtered_df)


dept_avg_salary = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:\n", dept_avg_salary)


sorted_df = df.sort_values(by='Salary', ascending=True)
print("\nSorted DataFrame by Salary:\n", sorted_df)

# Save to CSV
sorted_df.to_csv("sorted_employees.csv", index=False)
print("\nData saved to 'sorted_employees.csv'")

