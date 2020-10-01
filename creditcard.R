summary('creditcard.(2)')
str('creditcard.(2)')
attach('creditcard.(2)')
logit =glm('creditcard.(2)'~factor(age)+factor(income)+factor(share)+factor(expenditure)+factor(owner)+factor(selfemp)+factor(dependents)+factor(months)+factor(majorcards)+factor(active),family = "binomial",data = 'creditcard.(2)')
summary(logit)
prob =predict(logit,type = c("response"),'creditcard.(2)')
prob
confusion<-table(prob>0.5,)
confusion
accuracy<-sum(dig(confusion)/sum(confusion))
accuracy
