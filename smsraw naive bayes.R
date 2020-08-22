install.packages("readr")
sms_raw_NB <- read.csv("C:/Users/Yogesh/Downloads/sms_raw_NB.csv")
View(sms_raw_NB)
library(readr)
str(sms_raw_NB$type)
sms_raw_NB$type<-factor(sms_raw_NB$type)
table(sms_raw_NB$type)
install.packages("tm")
library(tm)
sms_Corpus <-Corpus(VectorSource(sms_raw_NB$text))
sms_Corpus<-tm_map(sms_Corpus,function(X) iconv(enc2utf8(X),sub = 'byte'))
Corpus_Clean<-tm_map(sms_Corpus, tolower)
Corpus_Clean<-tm_map(sms_Corpus, removeNumbers)
Corpus_Clean<-tm_map(sms_Corpus, removeWords, stopwords())
Corpus_Clean<-tm_map(sms_Corpus, removePanctuation)
Corpus_Clean<-tm_map(sms_Corpus, stripWitespace)
sms_dtm<-DocumentTermMatrix(Corpus_Clean)
sms_dtm
sms_raw_NB_train<-sms_raw_NB[1:4169,]
sms_raw_NB_test<-sms_raw_NB[4170:5559,]
sms_dtm_train<-sms_dtm[1:4169,]
sms_dtm_test<-sms_dtm[4170,5559,]
sms_Corpus_train<-Corpus_Clean[1:4169]
sms_Corpus_test<-Corpus_Clean[4170:5559]
prop.table(table(sms_raw_NB_test$type))
prop.table(table(sms_raw_NB_train$type))
sms_dict<-findFreqTerms(sms_dtm_train, 5)
sms_train<-DocumentTermMatrix(sms_Corpus_train,list(dictionary =sms_dict))
sms_test<-DocumentTermMatrix(sms_Corpus_test,list(dictionary =sms_dict))
convert_counts <-function(x){
  x<-ifelse(x>0,1,0)
  x<-factor(x, levels = c(0,1), labels = c("NO","YES"))
}
sms_train<-apply(sms_train, MARGIN = 2,convert_counts)
sms_test<-apply(sms_train, MARGIN = 2,convert_counts)
install.packages("e1071")
library(e1071)
sms_classifier<-naiveBayes(sms_train, sms_raw_NB_train$type)
sms_test_pred<-predict(sms_classifier, sms_test)
table(sms_test_pred)
prop.table(table(sms_test_pred))
install.packages("gmodels")
library(gmodels)
CrossTable(sms_test_pred, sms_raw_NB_test$type, 
           prop.chisq = FALSE, prop.t = FALSE, prop.r = FALSE,
           dnn = c('predicated', 'actual'))
