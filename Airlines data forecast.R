library(readxl)
Airlines_Data <- read_excel("C:/Users/Yogesh/Downloads/Airlines+Data (1).xlsx")
View(Airlines_Data)
X <- data.frame(outer(rep(month.abb,length = 96), month.abb,"==") + 0 )
colnames(X) <- month.abb
View(X)
Airlines_Data <- cbind(Airlines_Data,X)
View(Airlines_Data)
colnames(Airlines_Data)
Airlines_Data["t"] <- c(1:96)
View(Airlines_Data)

Airlines_Data["log_passengers"] <- log(Airlines_Data["Passengers"])
Airlines_Data["t_square"] <- Airlines_Data["t"]*Airlines_Data["t"]
View(Airlines_Data)
attach(Airlines_Data)
train <- Airlines_Data[1:70,]
test <- Airlines_Data[71:96,]
linear_model <- lm(Passengers ~ t, data = train)
summary(linear_model)
linear_pred <- data.frame(predict(linear_model, interval='predict', newdata =test))
rmse_linear <- sqrt(mean((test$Passengers-linear_pred$fit)^2, na.rm = T))
rmse_linear
expo_model <- lm(log_passengers ~ t, data = train)
summary(expo_model)
expo_pred <- data.frame(predict(expo_model, interval='predict', newdata = test))
rmse_expo <- sqrt(mean((test$Passengers-exp(expo_pred$fit))^2, na.rm = T))
rmse_expo
Quad_model <- lm(Passengers ~ t + t_square, data = train)
summary(Quad_model)
Quad_pred <- data.frame(predict(Quad_model, interval='predict', newdata=test))
rmse_Quad <- sqrt(mean((test$Passengers-Quad_pred$fit)^2, na.rm=T))
rmse_Quad
sea_add_model <- lm(Passengers ~ Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov, data = train)
summary(sea_add_model)
sea_add_pred <- data.frame(predict(sea_add_model, newdata=test, interval = 'predict'))
rmse_sea_add <- sqrt(mean((test$Passengers-sea_add_pred$fit)^2, na.rm = T))
rmse_sea_add
Add_sea_Quad_model <- lm(Passengers ~ t+t_square+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov, data = train)
summary(Add_sea_Quad_model)
Add_sea_Quad_pred <- data.frame(predict(Add_sea_Quad_model, interval='predict', newdata=test))
rmse_Add_sea_Quad <- sqrt(mean((test$Passengers - Add_sea_Quad_pred$fit)^2, na.rm=T))
rmse_Add_sea_Quad
multi_sea_model <- lm(log_passengers ~ Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov, data = train)
summary(multi_sea_model)
multi_sea_pred <- data.frame(predict(multi_sea_model, newdata=test, interval='predict'))
rmse_multi_sea <- sqrt(mean((test$Passengers-exp(multi_sea_pred$fit))^2, na.rm = T))
rmse_multi_sea
table_rmse <- data.frame(c("rmse_linear","rmse_expo","rmse_Quad","rmse_sea_add","rmse_Add_sea_Quad","rmse_multi_sea"),c(rmse_linear,rmse_expo,rmse_Quad,rmse_sea_add,rmse_Add_sea_Quad,rmse_multi_sea))
colnames(table_rmse) <- c("model","RMSE")
View(table_rmse)
write.csv(Airlines_Data, file="Airlines_Data.csv", row.names = F)
getwd()
Add_sea_Quad_model_final <- lm(Passengers ~ t+t_square+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov, data = Airlines_Data)
summary(Add_sea_Quad_model_final)
test_data <- read.csv(file.choose(),1)
View(test_data)
pred_new <- predict(Add_sea_Quad_model_final, newdata = test_data, interval = 'predict')
pred_new <- as.data.frame(pred_new)
plot(Add_sea_Quad_model_final)
acf(Add_sea_Quad_model_final$residuals, lag.max = 10)
A <- arima(Add_sea_Quad_model_final$residuals, order = c(1,0,0))
A$residuals
ARerrors <- A$residuals
acf(ARerrors, lag.max = 10)
install.packages("forecast")
library(forecast)
errors_12 <- forecast(A, h = 12)
future_errors <- data.frame(errors_12)
class(future_errors)
future_errors <- future_errors$Point.Forecast
View(future_errors)
