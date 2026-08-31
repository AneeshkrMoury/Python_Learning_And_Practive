import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score




#1. loading data
df = pd.read_csv('stress_data.csv')
# print(df.head())

#2 features and target
X = df[['Heart_Rate','Step_Count','Sleep_Duration']]
y = df['Stress_Level']

#3. scale features 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#4. train-test-split

X_train, X_test, y_train, y_test, = train_test_split(X_scaled, y, test_size=0.2, random_state=42
)

#train model
model = LinearRegression()
model.fit(X_train, y_train)

#predictions
y_pred = model.predict(X_test)

# print()
# print("Y predictions :", y_pred)
# print("Y actual value:", y_test.values)

print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

#calculate for new data point
new_data = [[61.95,8124,6.44]]
new_data_scaled = scaler.transform(new_data)

predicted_stress = model.predict(new_data_scaled)
print("Predicted Stress Level for new data point", predicted_stress[0])
