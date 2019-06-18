
setwd("C:\webDev\pycharm\dieta\data")


library(dplyr)

ak_symptoms <- read.csv("C:/webDev/pycharm/dieta/data/ak_symptoms.csv")
ak_triggers <- read.csv("C:/webDev/pycharm/dieta/data/ak_triggers.csv")
ta_symptoms <- read.csv("C:/webDev/pycharm/dieta/data/ta_symptoms.csv")
ta_triggers <- read.csv("C:/webDev/pycharm/dieta/data/ta_triggers.csv")

ak_symp_trig <- union_all(ak_symptoms, ak_triggers)
ta_symp_trig <- union_all(ta_symptoms, ta_triggers)
combined_ak_ta <- union_all(ak_symp_trig, ta_symp_trig)

write.csv(combined_ak_ta, file= "combined_ak_ta.csv")

getwd()

