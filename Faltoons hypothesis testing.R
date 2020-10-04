Faltoons <- read.csv("C:/Users/Yogesh/Downloads/Faltoons (1).csv")
View(Faltoons)
attach(Faltoons)
table1 <- table(Weekdays,Weekend)
table1              
prop.test(x=c(47,66),n=c(120,167),conf.level = 0.95,correct = FALSE, alternative = "two.sided")
prop.test(x=c(47,66),n=c(120,167),conf.level = 0.95,correct = FALSE,alternative = "less")
