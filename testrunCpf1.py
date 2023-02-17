print(f"""Please enter your age followed by current month salary (for incomplete month) accordingly.""")
user_age = int(input("age > "))
incompleteMonthSalary = int(input("Salary > "))

confirmationLoop = 1
while confirmationLoop < 3:
        confirmationInput = input(f"""Please confirm the entry, age ({user_age}) and salary this month ({incompleteMonthSalary}) by typing (Yes or No)
> """).lower()
        confirmationLoop += 1
        if confirmationInput == "yes":
            if incompleteMonthSalary < 50:
                print("Salary range does not require CPF contribution.")
            elif user_age <= 55:
                CpfBreakDownSelf = incompleteMonthSalary * 0.20
                CpfBreakdownEmployer = incompleteMonthSalary * 0.17
                TotalContribution = CpfBreakdownEmployer + CpfBreakDownSelf
                RemainingSalary = incompleteMonthSalary * 0.80
                FormatResponseOne = """
Self-contribution = {0}
Employer-Contribution = {1}
Total contribution = {2}
Remaining Salary = {3}
"""
                print(FormatResponseOne.format(CpfBreakDownSelf, CpfBreakdownEmployer, TotalContribution, RemainingSalary))
            elif user_age <= 60:
                CpfBreakDownSelf = incompleteMonthSalary * 0.15
                CpfBreakdownEmployer = incompleteMonthSalary * 0.145
                TotalContribution = CpfBreakdownEmployer + CpfBreakDownSelf
                RemainingSalary = incompleteMonthSalary * 0.85
                FormatResponseOne = """
Self-contribution = {0}
Employer-Contribution = {1}
Total contribution = {2}
Remaining Salary = {3}
"""
                print(FormatResponseOne.format(CpfBreakDownSelf, CpfBreakdownEmployer, TotalContribution, RemainingSalary))
            elif user_age <= 65:
                CpfBreakDownSelf = incompleteMonthSalary * 0.11
                CpfBreakdownEmployer = incompleteMonthSalary * 0.095
                TotalContribution = CpfBreakdownEmployer + CpfBreakDownSelf
                RemainingSalary = incompleteMonthSalary * 0.89
                FormatResponseOne = """
Self-contribution = {0}
Employer-Contribution = {1}
Total contribution = {2}
Remaining Salary = {3}
"""
                print(FormatResponseOne.format(CpfBreakDownSelf, CpfBreakdownEmployer, TotalContribution, RemainingSalary))
            elif user_age <= 70:
                CpfBreakDownSelf = incompleteMonthSalary * 0.07
                CpfBreakdownEmployer = incompleteMonthSalary * 0.085
                TotalContribution = CpfBreakdownEmployer + CpfBreakDownSelf
                RemainingSalary = incompleteMonthSalary * 0.93
                FormatResponseOne = """
Self-contribution = {0}
Employer-Contribution = {1}
Total contribution = {2}
Remaining Salary = {3}
"""
                print(FormatResponseOne.format(CpfBreakDownSelf, CpfBreakdownEmployer, TotalContribution, RemainingSalary))
            elif user_age >= 71:
                CpfBreakDownSelf = incompleteMonthSalary * 0.05
                CpfBreakdownEmployer = incompleteMonthSalary * 0.075
                TotalContribution = CpfBreakdownEmployer + CpfBreakDownSelf
                RemainingSalary = incompleteMonthSalary * 0.95
                FormatResponseOne = """
Self-contribution = {0}
Employer-Contribution = {1}
Total contribution = {2}
Remaining Salary = {3}
"""
                print(FormatResponseOne.format(CpfBreakDownSelf, CpfBreakdownEmployer, TotalContribution, RemainingSalary))
            break
        elif confirmationInput == "no":
            print("Please enter your (age) and (current month salary) once more.")
            user_age_reaffirm = int(input("age > "))
            incompleteMonthSalaryReaffirm = int(input("salary > "))
            AfterConfirmationOfEntry = user_age = user_age_reaffirm
            reaffirmingOnceMore = "You've entered age ({}), and salary ({}), thank you for affirmation."
            print(reaffirmingOnceMore.format(user_age_reaffirm, incompleteMonthSalaryReaffirm))
            if incompleteMonthSalaryReaffirm < 50:
                print("Salary range does not require CPF contribution.")
                break
            elif user_age_reaffirm <= 55:
                CpfBreakDownSelf = incompleteMonthSalaryReaffirm * 0.20
                CpfBreakdownEmployer = incompleteMonthSalaryReaffirm * 0.17
                TotalContribution = CpfBreakdownEmployer + CpfBreakDownSelf
                RemainingSalary = incompleteMonthSalaryReaffirm * 0.80
                FormatResponseOne = """
Self-contribution = {0}
Employer-Contribution = {1}
Total contribution = {2}
Remaining Salary = {3}
"""
                print(FormatResponseOne.format(CpfBreakDownSelf, CpfBreakdownEmployer, TotalContribution, RemainingSalary))
            elif user_age_reaffirm <= 60:
                CpfBreakDownSelf = incompleteMonthSalaryReaffirm * 0.15
                CpfBreakdownEmployer = incompleteMonthSalaryReaffirm * 0.145
                TotalContribution = CpfBreakdownEmployer + CpfBreakDownSelf
                RemainingSalary = incompleteMonthSalaryReaffirm * 0.85
                FormatResponseOne = """
Self-contribution = {0}
Employer-Contribution = {1}
Total contribution = {2}
Remaining Salary = {3}
"""
                print(FormatResponseOne.format(CpfBreakDownSelf, CpfBreakdownEmployer, TotalContribution, RemainingSalary))
            elif user_age_reaffirm <= 65:
                CpfBreakDownSelf = incompleteMonthSalaryReaffirm * 0.11
                CpfBreakdownEmployer = incompleteMonthSalaryReaffirm * 0.095
                TotalContribution = CpfBreakdownEmployer + CpfBreakDownSelf
                RemainingSalary = incompleteMonthSalaryReaffirm * 0.89
                FormatResponseOne = """
Self-contribution = {0}
Employer-Contribution = {1}
Total contribution = {2}
Remaining Salary = {3}
"""
                print(FormatResponseOne.format(CpfBreakDownSelf, CpfBreakdownEmployer, TotalContribution, RemainingSalary))
            elif user_age_reaffirm <= 70:
                CpfBreakDownSelf = incompleteMonthSalaryReaffirm * 0.07
                CpfBreakdownEmployer = incompleteMonthSalaryReaffirm * 0.085
                TotalContribution = CpfBreakdownEmployer + CpfBreakDownSelf
                RemainingSalary = incompleteMonthSalaryReaffirm * 0.93
                FormatResponseOne = """
Self-contribution = {0}
Employer-Contribution = {1}
Total contribution = {2}
Remaining Salary = {3}
"""
                print(FormatResponseOne.format(CpfBreakDownSelf, CpfBreakdownEmployer, TotalContribution, RemainingSalary))
            elif user_age_reaffirm >= 71:
                CpfBreakDownSelf = incompleteMonthSalaryReaffirm * 0.05
                CpfBreakdownEmployer = incompleteMonthSalaryReaffirm * 0.075
                TotalContribution = CpfBreakdownEmployer + CpfBreakDownSelf
                RemainingSalary = incompleteMonthSalaryReaffirm * 0.95
                FormatResponseOne = """
Self-contribution = {0}
Employer-Contribution = {1}
Total contribution = {2}
Remaining Salary = {3}
"""
                print(FormatResponseOne.format(CpfBreakDownSelf, CpfBreakdownEmployer, TotalContribution, RemainingSalary))
            break