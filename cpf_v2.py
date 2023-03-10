class calculate_CPF:

    def __init__(self, salary=0, age=0):
        self.salary = float(input("Enter your salary: "))
        self.age = int(input("Enter your current age: "))

    def calculate_cpf_contribution(self):
        global epee
        global formatted_display
        if (self.salary <= 49):
            formatted_display = f"You've entered '{self.salary}', note that such salary range doesn't required CPF contribution."
        elif (self.age < 55):
            eper, epee = self.salary * 0.17, self.salary * 0.20
            salary_remain = self.salary - epee
            formatted_display = f"Employer contribution: ${eper:.2f}, self contribution: ${epee:.2f} and the remaining salary: ${salary_remain:.2f}."
        elif (self.age >= 55) and (self.age <= 60):
            eper, epee = self.salary * 0.145, self.salary * 0.15
            salary_remain = self.salary - epee
            formatted_display = f"Employer contribution: ${eper:.2f}, self contribution: ${epee:.2f} and the remaining salary: ${salary_remain:.2f}."
        elif (self.age >= 61) and (self.age <= 65):
            eper, epee = self.salary * 0.11, self.salary * 0.095
            salary_remain = self.salary - epee
            formatted_display = f"Employer contribution: ${eper:.2f}, self contribution: ${epee:.2f} and the remaining salary: ${salary_remain:.2f}."
        elif (self.age >= 66) and (self.age <= 70):
            eper, epee = self.salary * 0.085, self.salary * 0.07
            salary_remain = self.salary - epee
            formatted_display = f"Employer contribution: ${eper:.2f}, self contribution: ${epee:.2f} and the remaining salary: ${salary_remain:.2f}."
        else:
            eper, epee = self.salary * 0.075, self.salary * 0.05
            salary_remain = self.salary - epee
            formatted_display = f"Employer contribution: ${eper:.2f}, self contribution: ${epee:.2f} and the remaining salary: ${salary_remain:.2f}."

    def cpf_allocation_method(self):
        if (self.salary <= 49):
            return formatted_display
        else:
            calculate_oa_sa_ma = input("""Would you also like to calculate the 'Oa, Sa and Ma' allocation?
Type 'yes' to continue, otherwise 'no': """).lower()
            if calculate_oa_sa_ma == 'yes':
                if (self.age <= 35):
                    oa = epee * 0.6217
                    sa = epee * 0.1621
                    ma = epee * 0.2162
                    formatted_display_2 = f"""The allocation would have been as followed; 
Ordinary Account (Oa): [${oa:.2f}]
Special Account (Sa): [${sa:.2f}]
MedicalSave Account (Ma): [${ma:.2f}]."""
                elif (self.age >= 45) and (self.age <= 50):
                    oa = epee * 0.5136
                    sa = epee * 0.2162
                    ma = epee * 0.2702
                    formatted_display_2 = f"""The allocation would have been as followed; 
Ordinary Account (Oa): [${oa:.2f}]
Special Account (Sa): [${sa:.2f}]
MedicalSave Account (Ma): [${ma:.2f}]."""
                elif (self.age >= 51) and (self.age <= 55):
                    oa = epee * 0.4055
                    sa = epee * 0.3108
                    ma = epee * 0.2837
                    formatted_display_2 = f"""The allocation would have been as followed; 
Ordinary Account (Oa): [${oa:.2f}]
Special Account (Sa): [${sa:.2f}]
MedicalSave Account (Ma): [${ma:.2f}]."""
                elif (self.age >= 56) and (self.age <= 60):
                    oa = epee * 0.4286
                    sa = epee * 0.1964
                    ma = epee * 0.375
                    formatted_display_2 = f"""The allocation would have been as followed; 
Ordinary Account (Oa): [${oa:.2f}]
Special Account (Sa): [${sa:.2f}]
MedicalSave Account (Ma): [${ma:.2f}]."""
                elif (self.age >= 61) and (self.age <= 65):
                    oa = epee * 0.1893
                    sa = epee * 0.2432
                    ma = epee * 0.5675
                    formatted_display_2 = f"""The allocation would have been as followed; 
Ordinary Account (Oa): [${oa:.2f}]
Special Account (Sa): [${sa:.2f}]
MedicalSave Account (Ma): [${ma:.2f}]."""
                elif (self.age >= 66) and (self.age <= 70):
                    oa = epee * 0.0715
                    sa = epee * 0.1785
                    ma = epee * 0.75
                    formatted_display_2 = f"""The allocation would have been as followed; 
Ordinary Account (Oa): [${oa:.2f}]
Special Account (Sa): [${sa:.2f}]
MedicalSave Account (Ma): [${ma:.2f}]."""
                else:
                    oa = epee * 0.08
                    sa = epee * 0.08
                    ma = epee * 0.84
                    formatted_display_2 = f"""The allocation would have been as followed; 
Ordinary Account (Oa): [${oa:.2f}]
Special Account (Sa): [${sa:.2f}]
MedicalSave Account (Ma): [${ma:.2f}]."""
                display_response = f"""{formatted_display}
{formatted_display_2}"""
                return display_response
            else:
                return formatted_display


x = calculate_CPF()
x.calculate_cpf_contribution()
print(x.cpf_allocation_method())
