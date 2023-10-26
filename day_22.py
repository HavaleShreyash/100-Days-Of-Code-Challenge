import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary']*2

    return employees
    
if __name__ == "__main__":
    employees = pd.DataFrame(
        [
            ["John", "Doe", 100000],
            ["Jane", "Doe", 100001],
            ["Billy", "Bob", 99999],
        ],
        columns=["first_name", "last_name", "salary"],
    )
    print(employees)
    employees = modifySalaryColumn(employees)
    print(employees)