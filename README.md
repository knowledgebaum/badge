
#Simple Badges


## Getting Started
Clone the repository.  Go into the badge folder.

 ###To run

 At command prompt type:
* python simple_badge_module.py 1

Or

* python simple_runner.py 

###To test

python test_simple_badge.py

###Note

 simple_badge_module arguments are 1 or 2 ( where 1 = AK, 2 = TA).



## Columns Inputs

This script expects a .csv with these columns: ts,symptom,intensity,duration,day,week,month,trigger,person

## Outputs

###STATS

person,
total_symptom_enteries,
total_food_enteries,
total_enteries,
first_entery,
last_entry,
number_days_with_enteries,

###BADGES

rank,
complex_diet,
archivist,
coffee,
gluten,
lactose,
lectin

# Badges

This project aims to gamify the Dieta app by providing users badges for certain thresholds achieved when recording  their user data.
It takes input data from Dieta and outputs user stats, and various badges based on diet, 
(like how frequently users add 
information to the app, and the total number of enteries users have made.)

## Getting Started

Clone the repository.  Go into the badge folder.  Run runner.py to demo the badgeModule (which contains the Badge class) on the provided data.  (You will have to change the sympPath and trigPath to the correct path for ak_symptoms, ak_triggers for your system file structure. )



### Tests in Test_Simple_Badge


Test provided data 
1. Rank of provided data is 5
2. Complex Data Badge is true
3. Archivist Badge is true 
4. Coffee Badge is true
5. Gluten Badge is true
6. Lactose Badge is true
7. Lectin Badge is True
