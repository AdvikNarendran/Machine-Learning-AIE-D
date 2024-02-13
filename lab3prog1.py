import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def classifier(df):
    features = ["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]
    X = df[features]
    y = df['Category']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    df['Predicted Category'] = classifier.predict(X)
    return df
df = pd.read_excel('Lab Session1 Data.xlsx')

col=["Candies (#)","Mangoes (Kg)","Milk Packets (#)"]
data_matrix = df[col]
A=data_matrix.values
row,col=A.shape
print("dimensionality of A is ",col)
print("number of vectors A is ",row)
C=df[["Payment (Rs)"]].values

rank = np.linalg.matrix_rank(A)
print("rank of A is", rank)

pinvA= np.linalg.pinv(A)

print(f"\n\npseudoinverse of A is \n{pinvA}\n\n\n")


X= pinvA @ C

print(f"Cost of one candy is Rs {round(X[0][0])}")
print(f"Cost of onne kg mango is Rs {round(X[1][0])}")
print(f"Cost of one milk packet is Rs {round(X[2][0])}")

df['Category'] = df['Payment (Rs)'].apply(lambda x: 'RICH' if x > 200 else 'POOR')
df=classifier(df)
print(df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)', 'Payment (Rs)', 'Category', 'Predicted Category']])

