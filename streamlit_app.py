import kagglehub
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

path = kagglehub.dataset_download("janiobachmann/bank-marketing-dataset", path="bank.csv")

df = pd.read_csv(path)

x = df[df.columns.drop(["deposit"])]
y = df["deposit"]

xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size=0.2, random_state=42)

py = len(ytrain[ytrain=="yes"])/len(ytrain)

num = ["age", "balance", "duration", "campaign", "pdays", "previous"]

pxy = pd.concat({col: xtrain[col].loc[ytrain=="yes"].value_counts()/len(ytrain[ytrain=="yes"]) if col not in num else pd.Series({"var": np.var(xtrain[col].loc[ytrain=="yes"]), "mu": np.mean(xtrain[col].loc[ytrain=="yes"])}) for col in xtrain.columns}).rename("count")

#st.write(pxy)
st.write('''## Probabilities of P(x|y)''')
pxy.groupby(level=0).apply(lambda p:st.bar_chart(p.droplevel(0)).title=p.name if p.name not in num else st.pyplot((lambda f:(f.gca().plot(x:= np.linspace(p.xs("mu", level=1).iloc[0]-4*np.sqrt(p.xs("var", level=1).iloc[0]), p.xs("mu",level=1).iloc[0]+4*np.sqrt(p.xs("var", level=1).iloc[0]),500),np.exp(-(x-p.xs("mu",level=1).iloc[0])**2/(2*p.xs("var", level=1).iloc[0]))/np.sqrt(2*np.pi*p.xs("var", level=1).iloc[0])),f.gca().set_title(p.name), f)[1])(plt.figure())))
