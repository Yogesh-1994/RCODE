import pandas as pd
Amtrak = pd.read_csv("C:\\Users\\Yogesh\\Desktop\\Wallmart input.csv")
month =['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'] 
import numpy as np
p = Amtrak["Month"][0]
Amtrak['months']= 0
for i in range(159):
    p = Amtrak["Month"][i]
    Amtrak['months'][i]= p[0:3]
month_dummies = pd.DataFrame(pd.get_dummies(Amtrak['months']))
Amtrak1 = pd.concat([Amtrak,month_dummies],axis = 1)
Amtrak1["t"] = np.arange(1,160)
Amtrak1["t_squared"] = Amtrak1["t"]*Amtrak1["t"]
Amtrak1.columns
Amtrak1["log_Footfalls"] = np.log(Amtrak1["Footfalls"])
Amtrak1.rename(columns={"Footfalls ": 'Footfalls'}, inplace=True)
Amtrak1.Footfalls.plot()
Train = Amtrak1.head(147)
Test = Amtrak1.tail(12)
import statsmodels.formula.api as smf 
linear_model = smf.ols('Footfalls~t',data=Train).fit()
pred_linear =  pd.Series(linear_model.predict(pd.DataFrame(Test['t'])))
rmse_linear = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_linear))**2))
rmse_linear
Exp = smf.ols('log_Footfalls~t',data=Train).fit()
pred_Exp = pd.Series(Exp.predict(pd.DataFrame(Test['t'])))
rmse_Exp = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Exp)))**2))
rmse_Exp
Quad = smf.ols('Footfalls~t+t_squared',data=Train).fit()
pred_Quad = pd.Series(Quad.predict(Test[["t","t_squared"]]))
rmse_Quad = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_Quad))**2))
rmse_Quad
add_sea = smf.ols('Footfalls~Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_add_sea = pd.Series(add_sea.predict(Test[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov']]))
rmse_add_sea = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_add_sea))**2))
rmse_add_sea
add_sea_Quad = smf.ols('Footfalls~t+t_squared+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_add_sea_quad = pd.Series(add_sea_Quad.predict(Test[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','t','t_squared']]))
rmse_add_sea_quad = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_add_sea_quad))**2))
rmse_add_sea_quad 
Mul_sea = smf.ols('log_Footfalls~Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data = Train).fit()
pred_Mult_sea = pd.Series(Mul_sea.predict(Test))
rmse_Mult_sea = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Mult_sea)))**2))
rmse_Mult_sea
Mul_Add_sea = smf.ols('log_Footfalls~t+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data = Train).fit()
pred_Mult_add_sea = pd.Series(Mul_Add_sea.predict(Test))
rmse_Mult_add_sea = np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_Mult_add_sea)))**2))
rmse_Mult_add_sea 
data = {"MODEL":pd.Series(["rmse_linear","rmse_Exp","rmse_Quad","rmse_add_sea","rmse_add_sea_quad","rmse_Mult_sea","rmse_Mult_add_sea"]),"RMSE_Values":pd.Series([rmse_linear,rmse_Exp,rmse_Quad,rmse_add_sea,rmse_add_sea_quad,rmse_Mult_sea,rmse_Mult_add_sea])}
table_rmse=pd.DataFrame(data)
table_rmse
predict_data = pd.read_csv("D:\\Data Science Study\\Data science assignment files\\Predict_new.csv")
pred_new  = pd.Series(Quad.predict(predict_data))
pred_new
predict_data["forecasted_Footfalls"] = pd.Series(pred_new)
