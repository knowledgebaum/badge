from pathlib import Path
import pandas as pd
import numpy as np
import os.path
import sys


#######Load CSV#####
def load_csv():
    dirname = os.getcwd()
    csv_path =  "C\webDev\pycharm\dieta\\badge\data\\final_combined_ak_ta.csv"
    if not os.path.exists(csv_path):
        csv_path = os.path.join(dirname, "data\\final_combined_ak_ta.csv")

#    print(csv_path)
    users_data = pd.read_csv(csv_path)
    return users_data

users_data = load_csv()

def get_args():
    try:
        person_arg = sys.argv[1]
    except:
        print('Please add user number (1 or 2 ) as an argument to indicate the person you are choosing')
    return person_arg


#
# if len(sys.argv) == 3:
#     csv_path = sys.argv[2]
#     if not os.path.exists(csv_path):
#         print("The path entered ("+ csv_path + ") does not work")
# else:
#     csv_path = "C\webDev\pycharm\dieta\\badge\data\\final_combined_ak_ta.csv"
#     if not os.path.exists(csv_path):
#         csv_path = "badge/data/final_combined_ak_ta.csv"

def get_person_dataframe(person, csv=users_data):
    #split dataframe
    person_data_frame = csv[csv.person == person]

    return pd.DataFrame(person_data_frame)



def get_rank_badge(person, users_df=users_data):
    df = get_person_dataframe(person, users_df)
    total_enteries = len(df)

    # cut off values for RANK BADGES
    newbVal = 10
    initVal = 15
    casVal = 25
    enthusVal = 50
    scholVal = 100
    mastVal = 1000

    # newbie
    if total_enteries >= newbVal and total_enteries < initVal:
        return 1
    # Initiate Research
    elif total_enteries >= initVal and total_enteries < casVal:
        return 2
    # Casual Researcher
    elif total_enteries >= casVal and total_enteries < enthusVal:
        return 3
    # Research Enthusiast
    elif total_enteries >= enthusVal and total_enteries < scholVal:
        return 4
    # Scholar
    elif total_enteries >= scholVal and total_enteries < mastVal:
        return 5
    # Master Researcher
    elif total_enteries >= mastVal:
        return 6
    else:
        return 'broke'



def get_complex_diet_badge(person, users_df=users_data):

    df = get_person_dataframe(person, users_df)
    COMPLEX_DIET_VAL = 50

    # print(trig_df.head()) Just seeing if everything worked
    complexDiet = df['trigger'].count()  # changed from nunique
    result = complexDiet

    if result > COMPLEX_DIET_VAL:
        return True
    else:
        return False

##ARCHIVIST BADGE
def get_archivist_badge(person, users_df=users_data):
    df = get_person_dataframe(person, users_df)
    ARCHIVIST_VAL = 20

    max_enteries_per_day = df.groupby(['day'])[['symptom', 'trigger']].count()

    max_enteries_per_day  ## see data frame
    ##create sum_symp_trig column out of symptom and trigger column
    max_enteries_per_day['sum_symp_trig'] = max_enteries_per_day['symptom'] + max_enteries_per_day['trigger']

    # extract the maximum value as an int from sum_symp_trig
    result = max_enteries_per_day['sum_symp_trig'].max().item()

    if result > ARCHIVIST_VAL:
        return True
    else:
        return False


####################
# DIET CATEGORY BADGES
####################

#DIET CATEGORYS DICTIONARYS
coffee = {
  'category': 'coffee',
  'terms': ['coffee', 'latte', 'americano', 'espresso',
    'breve', 'cappucino', 'mocha', 'macchiato'
  ]
}
gluten = {
  'category': 'gluten',
  'terms': ['bread', 'pasta', 'sour dough', 'macaroni', 'wheat', 'gnocchi',
    'pretzels', 'pancakes', 'waffles', 'biscuits'
  ]
}
lactose = {
  'category': 'lactose',
  'terms': ['milk', 'cheese', 'yogurt', 'alfredo']
}
lectin = {
  'category': 'lectin',
  'terms': ['potato', 'tomato', ]
}

def apply_diet_filter(df, diet):


    df['trigger'] = df['trigger'].str.lower()
    filter = df['trigger'].isin(diet)
    category_count = len(df[filter])
    #print('diet count :' + category_count)
    if category_count > 0:
        return True
    else:
        return False

def get_coffee_badge(person, users_df=users_data):
    df = get_person_dataframe(person, users_df)
    items = coffee.get('terms')
    return apply_diet_filter(df, items)

def get_gluten_badge(person, users_df=users_data):
    df = get_person_dataframe(person, users_df)
    items = gluten.get('terms')
    return apply_diet_filter(df, items)

def get_lectin_badge(person, users_df=users_data):
    df = get_person_dataframe(person, users_df)
    items = lectin.get('terms')
    return apply_diet_filter(df, items)

def get_lactose_badge(person, users_df=users_data):
    df = get_person_dataframe(person, users_df)
    items = lactose.get('terms')
    return apply_diet_filter(df, items)


def get_user_stats(person, users_df=users_data):

    df = get_person_dataframe(person, users_df)
    person = person #df.iloc[0, 0]
    #entery_count = df.count()

    #.total_food_enteries = .entery_count.loc['trigger']
    total_food_enteries = df['trigger'].count()

    total_symptom_enteries = df['symptom'].count()#len(df['symptom']!='NA') #????

    total_enteries = len(df)

    number_days_with_enteries = len(df.day.unique())

    first_entery = min(df['day'])

    last_entry = max(df['day'])

    rank = get_rank_badge(person, users_df)

    complex_diet = get_complex_diet_badge(person, users_df)

    archivist = get_archivist_badge(person, users_df)

    coffee = get_coffee_badge(person, users_df)
    gluten = get_gluten_badge(person, users_df)
    lactose = get_lactose_badge(person, users_df)
    lectin = get_lectin_badge(person, users_df)


    table = {
        "User_ID": person,
        "tot_symp_stat": total_symptom_enteries,
        "tot_trig_stat": total_food_enteries,
        "tot_entery_stat": total_enteries,
        "first_entery": first_entery,
        "last_entery": last_entry,
        "Number of Days": number_days_with_enteries,
        "rank_badge": rank,
        "complex_diet_badge": complex_diet,
        "archivist_badge": archivist,
        "coffee_badge": coffee,
        "gluten_badge": gluten,
        "lactose_badge" : lactose,
        "lectin_badge" : lectin
            }
    return pd.DataFrame.from_dict(table, orient='index') # or table


###INSTANCE###

###COMMAND ARG VERSION

if len(sys.argv) > 1:
    print(get_user_stats(int(get_args()), users_data))


###MANUAL VERSION
""" print(get_user_stats(2, users_data))"""


"""  TO REWRITE
def get_rank_badge(person, users_df):

    df = get_person_dataframe(person, users_data)

    total_enteries = len(df)
    rank = [0, 10, 30, 90, 270, 810, 1620, 2430]

    for i in range(len(rank)-1):
        if total_enteries >= rank[i] and total_enteries < rank[i+1]:
            res = i
            print("kill" + i)
        elif total_enteries > len(rank) -1:
            res = len(rank) - 1
        else: print("error")
        return res
"""