# Program_9d.py: Black-Scholes Option Prices for Call/Put.
# Computing the Black-Scholes Greeks.
import numpy as np
from scipy.stats import norm
# Parameters: r=interest rate,S=underlying price ($),Strike price ($), 
#T=240/365 days, sigma=volatility, C=CALL, P=PUT.
r , S , K , T , sigma  = 0.01 , 30 , 40, 240/365 , 0.3
def Black_Scholes(r,S,K,T,sigma,type="C"):
  d1 = (np.log(S/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))
  d2 = d1 - sigma*np.sqrt(T)
  try:
    if type=="C":
      price=S*norm.cdf(d1,0,1)-K*np.exp(-r*T)*norm.cdf(d2,0,1)
      delta_calc=norm.cdf(d1,0,1)
      gamma_calc=norm.pdf(d1,0,1)/(S*sigma*np.sqrt(T))
      vega_calc=S*norm.pdf(d1,0,1)*np.sqrt(T)*0.01
      theta_calc=(-S*norm.pdf(d1,0,1)*sigma/(2*np.sqrt(T))-\
                  r*K*np.exp(-r*T)*norm.cdf(d2,0,1)) / 365
      rho_calc=K*T*np.exp(-r*T)*norm.cdf(d2,0,1)*0.01
    elif type=="P":
      price=K*np.exp(-r*T)*norm.cdf(-d2,0,1)-S*norm.cdf(-d1,0,1)
      delta_calc=-norm.cdf(-d1,0,1)
      gamma_calc=norm.pdf(d1,0,1)/(S*sigma*np.sqrt(T))
      vega_calc=S*norm.pdf(d1,0,1)*np.sqrt(T) * 0.01
      theta_calc=(-S*norm.pdf(d1,0,1)*sigma/(2*np.sqrt(T))-\
                  r*K*np.exp(-r*T)*norm.cdf(-d2,0,1)) / 365
      rho_calc=-K*T*np.exp(-r*T)*norm.cdf(-d2,0,1) * 0.01
    return [price,delta_calc,gamma_calc,vega_calc,theta_calc,rho_calc]
  except:
    print("Please input correct parameters")
BS_Call=Black_Scholes(r,S,K,T,sigma,type="C")
BS_Put=Black_Scholes(r,S,K,T,sigma,type="P")
print("r=",r,"S=",S,"K=",K,"T=",T,"sigma=",sigma)
print("Option CALL price is: ", round(BS_Call[0],2))
print("Option PUT price is: ", round(BS_Put[0],2))
print("delta Call is: ", round(BS_Call[1],4))
print("delta Put is: ", round(BS_Put[1],4))
print("gamma Call/Put is: ", round(BS_Call[2],4))
print("vega Call/Put is: ", round(BS_Call[3],4))
print("theta Call is: ", round(BS_Call[4],4))
print("theta Put is: ", round(BS_Put[4],4))