library(readxl)
JohnyTalkers <- read_excel("C:/Users/Yogesh/Downloads/JohnyTalkers.xlsx")
View(JohnyTalkers)
attach(JohnyTalkers)
table1 <- table(Drinks,Person)
table1              
prop.test(x=c(58,152),n=c(422,588),conf.level = 0.95,correct = FALSE, alternative = "two.sided")
prop.test(x=c(58,152),n=c(422,588),conf.level = 0.95,correct = FALSE,alternative = "less")
