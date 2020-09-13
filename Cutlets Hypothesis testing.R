Cutlets <- read.csv("C:/Users/Yogesh/Downloads/Cutlets.csv")
View(Cutlets)
attach(Cutlets)
table(Unit.A,Unit.B)
t2<-prop.table(table(Unit.B))
t1<-table(Unit.A)
t1
chisq.test(table(Unit.A,Unit.B))
