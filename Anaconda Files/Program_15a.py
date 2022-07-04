#Program_15a.py: Simple Linear Regression.
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import statsmodels.api as sm
import seaborn as sns
sns.set()
data=pd.read_csv("CO2_GDP_USA_Data.csv")
data.head()
plt.rcParams["font.size"] = "20"
y = np.array(data['co2 per capita (metric tons)'])
x = np.array(data['gdp per capita (USD)']).reshape((-1, 1))
plt.scatter(x , y , marker = "+" , color = "blue")
plt.ylabel('CO$_2$ Emissions Per Capita (Tons)')
plt.xlabel('GDP Per Capita (USD)')
regr = linear_model.LinearRegression()
regr.fit(x , y)
y_pred = regr.predict(x)
print("Gradient: \n", regr.coef_)
print("y-Intercept: \n", regr.intercept_)
print("MSE: %.2f"% mean_squared_error(y , y_pred))
print("R2 Score: %.2f" % r2_score(y , y_pred))
plt.plot(x , y_pred , color = "red")
plt.show()
sm.add_constant(x)
results = sm.OLS(y,x).fit()
print(results.summary())
