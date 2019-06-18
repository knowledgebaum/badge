
#setwd("C:\webDev\pycharm\dieta\data")


library(dplyr)

ak_symptoms <- read.csv("C:/webDev/pycharm/dieta/data/ak_symptoms.csv")
ak_triggers <- read.csv("C:/webDev/pycharm/dieta/data/ak_triggers.csv")
ta_symptoms <- read.csv("C:/webDev/pycharm/dieta/data/ta_symptoms.csv")
ta_triggers <- read.csv("C:/webDev/pycharm/dieta/data/ta_triggers.csv")



ak_symp_trig <- union_all(ak_symptoms, ak_triggers)
#add_column(ak_symp_trig, person="1")
ak_symp_trig$person <- rep(1,nrow(ak_symp_trig))
ta_symp_trig <- union_all(ta_symptoms, ta_triggers)
#add_column(ak_symp_trig, person="2")
ta_symp_trig$person <- rep(2,nrow(ta_symp_trig))

combined_ak_ta <- union_all(ak_symp_trig, ta_symp_trig)


write.csv(combined_ak_ta, file= "combined_ak_ta.csv")

getwd()

