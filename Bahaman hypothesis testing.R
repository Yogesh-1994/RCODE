library(readxl)
Bahaman <- read_excel("C:/Users/Yogesh/Downloads/Bahaman.xlsx")
View(Bahaman)
attach(Bahaman)
table(Country,Defective)
t2<-prop.table(table(Defective))
t1<-table(Country)
t1
chisq.test(table(Country,Defective))
