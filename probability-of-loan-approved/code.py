# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here

df = pd.read_csv(path)
df_fico= df[df['fico']>700]
p_a = len(df_fico)/len(df)
print(p_a)

df_purpose= df[df['purpose']=='debt_consolidation']
p_b = len(df_purpose)/len(df)
print(p_b)

df1 = df[df['purpose']=='debt_consolidation']

p_a_b = (len(df1[df['fico']>700])/len(df1))/p_a
print(p_a_b)

p_b_a = (len(df1[df['fico']>700])/len(df1))/p_b
print(p_b_a)

result = p_b_a==p_a
print(result)
# code ends here


# --------------
# code starts here
prob_lp = len(df[df['paid.back.loan']=='Yes'])/len(df)
prob_cs = len(df[df['credit.policy']=='Yes'])/len(df)

new_df = df[df['paid.back.loan']=='Yes']

prob_pd_cs = len(new_df[new_df['credit.policy']=='Yes'])/len(new_df)

bayes = prob_pd_cs * prob_lp / prob_cs

print(bayes)
# code ends here


# --------------
# code starts here
plt.bar(df['purpose'],df['paid.back.loan'])
df1 = df[df['paid.back.loan']=='No']

plt.bar(df1['purpose'],df1['paid.back.loan'])
plt.show()
# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()

plt.hist((inst_median,inst_mean),bins=8)
plt.hist(df['log.annual.inc'],bins=8)
plt.show()
# code ends here


