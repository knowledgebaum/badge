
library(cluster.datasets)
library(dplyr)   
library(NLP)

##DIET TYPES



#load data
####CSV####

ak_symptoms <- read.csv("C:/webDev/pycharm/dieta/rStudio/data/ak_symptoms.csv")


sympPath <- read.csv("C:/webDev/pycharm/dieta/rStudio/data/ak_symptoms.csv", header = T)
trigPath <- read.csv("C:/webDev/pycharm/dieta/rStudio/data/ak_triggers.csv", header = T)
full_data <- merge(sympPath, trigPath, all.x = T, all.y = T )

data(full_data)
#View(full_data)





#functions
get_user_stats <- function(full_data){
  
  View(full_data)
  #CSV Version
  
  total_food_enteries <- #nrow(select(trigger)) 
    full_data %>% 
    filter(!is.na(trigger))
  
  
  total_symptom_enteries <- #nrow(select(symptom)) 
    full_data %>% 
    filter(!is.na(symptom))
  
  
  total_enteries <- count(full_data)
  
  number_days_with_enteries <- count(distinct(full_data, day)) #nrow(distinct(full_data.day))
  
  first_entery <- first(select(full_data, day))
  
  
  last_entry <- last(select(full_data, day))
  
  
}

get_rank_badge <- function(){
  
  total_enteries <- count(fullData)
  
  #FOR LOOP VERSION  
  RANK_CUTTOFFS <- c(10,15,25,50,100,200) # list of cuttoff values 
  #(initiate, casual, enthusiast ... master )
  
  for(i in 1:6){ #runs over the 6 levels of research rank
    if(i < 6){ #runs 5 times then returns 6 on 6th time
      if(total_enteries <= RANK_CUTTOFFS[i])
      {
        return (i)#returns a number representing the badge
      }
      
    }
    else{
      return (6) #any number greater than
      break
    }
    
  }
  
} 


get_badge_boolean <- function(cut_value, query_result){
  if (query_result > cut_value  ) {
    return (TRUE)    
  }
  else{
    return (FALSE)
  }
}

get_complex_diet_badge<- function(){
  COMPLEX_DIET_THRESHOLD <- 50 
  query <- dplyr::n_distinct(dplyr::select(fullData, trigger))#
  print(query)
  result <-  get_badge_boolean(COMPLEX_DIET_THRESHOLD, query)
  return (result)
}

get_archivist_badge <- function(){
  #get max entieries per day for trigger, symptom
  ARCHIVIST_THRESHOLD <-20
  #query
  trigger_max <- group_by(full_data, day) %>%
    max(select(full_data, trigger))
  trigger_max
  symptom_max <-  group_by(full_data, day) %>%
    max(select(full_data, symptom))
  max_enteries_per_day <- trigger_max + symptom_max
  result = get_badge_boolean(ARCHIVIST_THRESHOLD, max_enteries_per_day)
  return(result)
}

apply_diet_filter <- function(filter_food){
  if(nrow(filter_food)>0){result<-TRUE}
  else{result<-FALSE}
  return(result)
}

get_coffee_badge <- function(){
  DIET_COFFEE <- C('coffee', 'latte', 'americano', 'espresso', 'breve', 'cappucino', 'mocha', 'macchiato')
  diet_items <- DIET_COFFEE
  #query
  food <- select(full_data, trigger)
  filter_food <- filter(food, diet_items %in% food) 
  result = apply_diet_filter(filter_food)
  return(result)
}

get_gluten_badge <- function(){
  DIET_GLUTEN <- C('bread', 'pasta', 'sour dough', 'macaroni', 'wheat', 'gnocchi',
                   'pretzels', 'pancakes', 'waffles', 'biscuits')
  diet_items <- DIET_GLUTEN
  food <- select(full_data, trigger)
  filter_food <- filter(food, diet_items %in% food) 
  result = apply_diet_filter(filter_food)
  return(result)
}

get_lectin_badge <- function(){
  DIET_LECTIN <- C('potato', 'tomato')
  diet_items <- DIET_LECTIN
  food <- select(full_data, trigger)
  filter_food <- filter(food, diet_items %in% food) 
  result = apply_diet_filter(filter_food)
  return(result)
}
get_lactose_badge <- function(){
  DIET_LACTOSE <- C('milk', 'cheese', 'yogurt', 'alfredo')
  diet_items <- DIET_LACTOSE
  food <- select(full_data, trigger)
  filter_food <- filter(food, diet_items %in% food) 
  result = apply_diet_filter(filter_food)
  return(result)
}

rank <- get_rank_badge()
archivist <- get_archivist_badge()
complex <- get_complex_diet_badge()
coffee <- get_coffee_badge()
gluten <- get_gluten_badge()
lactose <- get_lactose_badge()
lectin <- get_lectin_badge()


get_user_stats(full_data)

badge_name <- c("Rank", "Archivist", "Complex Diet", "Coffee", "Gluten", "Lactose", "Lectin")
#value <- list(get_rank_badge(), get_archivist_badge(),get_complex_diet_badge(), get_coffee_badge(), get_gluten_badge(), get_lactose_badge(), get_lectin_badge())
#value <- list(as.String(get_rank_badge() ), as.String(get_archivist_badge() ),as.String(get_complex_diet_badge() ), as.String(get_coffee_badge() ), as.String(get_gluten_badge() ), as.String(get_lactose_badge() ), as.String(get_lectin_badge() ))

#value
#rank = get_rank_badge()
#rank
value = list(as.integer(as.logical(get_archivist_badge())))

output_df <- data.frame(badge_name, value)
View(output_df)
