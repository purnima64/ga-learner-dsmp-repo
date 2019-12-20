# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
data = pd.read_csv(path)
bank = pd.DataFrame(data)
#print(bank)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)
# code ends here


# --------------
# code starts here
banks = bank.drop(columns='Loan_ID')
#banks.isnull().sum()
print(banks.isnull().sum())
bank_mode = banks.mode(axis='columns')
banks = bank_mode.fillna(0)
print(banks)
#code ends here


# --------------
# Code starts here


#print(banks)

avg_loan_amount = pd.pivot_table(banks, values='LoanAmount', index=['Gender', 'Married', 'Self_Employed'], aggfunc=np.mean)

print(avg_loan_amount)

# code ends here



# --------------
# code starts here
loan_approved_se = len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')])
loan_approved_nse = len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])
count = len(banks)

percentage_se = loan_approved_se *  100 /count
percentage_nse = loan_approved_nse * 100 /count

#print(loan_approved_se)
#print(loan_approved_nse)
print(percentage_se)
print(percentage_nse)
# code ends here


# --------------
# code starts here

#print(banks)
loan_term = banks['Loan_Amount_Term'].map(lambda b: (int(b)/12))
#print(loan_term)
banks['loan_term'] = loan_term

big_loan_term = len(banks[banks['loan_term']>=25])

print(big_loan_term)
# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History']
print(loan_groupby)

mean_values = loan_groupby.mean()
print(mean_values)
# code ends here


