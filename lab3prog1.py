'''Please refer to the “Purchase Data” worksheet of Lab Session1 Data.xlsx. Please load the data 
and segregate them into 2 matrices A & C (following the nomenclature of AX = C). Do the following 
activities. 
• What is the dimensionality of the vector space for this data? 
• How many vectors exist in this vector space? 
• What is the rank of Matrix A? 
• Using Pseudo-Inverse find the cost of each product available for sale.  
(Suggestion: If you use Python, you can use numpy.linalg.pinv() function to get a 
pseudo-inverse.) 
A2. Use the Pseudo-inverse to calculate the model vector X for predicting the cost of the products 
available with the vendor. 
A3. Mark all customers (in “Purchase Data” table) with payments above Rs. 200 as RICH and others 
as POOR. Develop a classifier model to categorize customers into RICH or POOR class based on 
purchase behavior. '''

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

