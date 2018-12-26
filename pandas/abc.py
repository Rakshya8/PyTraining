import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('loan_test.csv')

abc = df[['annual_income','loan_amount','funded_amount']]
abc.plot(kind='bar')