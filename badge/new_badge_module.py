from pathlib import Path
import pandas as pd
import numpy as np
import os.path


#Load CSV
csv_path =  "C:\webDev\pycharm\dieta\\badge\data\\final_combined_ak_ta.csv"
users_data = pd.read_csv(csv_path)


###TYPE USERS
print("###############****#####")
print(type(users_data))
####


def print_csv(csv):
    print(pd.DataFrame.head(csv))


#split_csv
def get_person_dataframe(person, csv=users_data):
    #split dataframe
    person_data_frame = csv[csv.person == person]


    return pd.DataFrame(person_data_frame)

person_data_frame= []

person_data_frame = get_person_dataframe(1, users_data)

###############
#get_rank_badge
def get_rank_badge(df=person_data_frame):
    # total_enteries = 12 #len(df)
    # rank_cutoff = [10,20,30,40,50,60,300]
    # for i in range(0, len(rank_cutoff)):
    #     if i == 0 and total_enteries <= rank_cutoff[0]:
    #         return i + 1 # rank starts at 1 (index starts at 0)
    #     elif i>0 and total_enteries >= rank_cutoff[i]: #and total_enteries <= rank_cutoff[i-1]:
    #         return i + 1 # rank starts at 1 (index starts at 0)
    #     else:
    #         print('Rank error')

    total_enteries = len(df)

    # cut off values for RANK BADGES
    newbVal = 10
    initVal = 15
    casVal = 25
    enthusVal = 50
    scholVal = 100
    mastVal = 200

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


#MISC BADGES

##COMPLEX DIET BADGE

def get_complex_diet_badge(df=person_data_frame):

    COMPLEX_DIET_VAL = 50

    # print(trig_df.head()) Just seeing if everything worked
    complexDiet = df['trigger'].count()  # changed from nunique
    result = complexDiet

    if result > COMPLEX_DIET_VAL:
        return True
    else:
        return False

##ARCHIVIST BADGE
def get_archivist_badge(df=person_data_frame):

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
coffee = {'category': 'coffee', 'terms': ['coffee', 'latte', 'americano', 'espresso',
                                                'breve', 'cappucino', 'mocha', 'macchiato']}
gluten = {'category': 'gluten', 'terms': ['bread', 'pasta', 'sour dough', 'macaroni', 'wheat', 'gnocchi',
                                                'pretzels', 'pancakes', 'waffles', 'biscuits']}
lactose = {'category': 'lactose', 'terms': ['milk', 'cheese', 'yogurt', 'alfredo']}
lectin = {'category': 'lectin', 'terms': ['potato', 'tomato', ]}

def apply_diet_filter(df, diet):

    df['trigger'] = df['trigger'].str.lower()
    filter = df['trigger'].isin(diet)
    category_count = len(df[filter])

    if category_count > 0:
        return True
    else:
        return False

def get_coffee_badge(df=person_data_frame):
    items = coffee.get('terms')
    return apply_diet_filter(df, items)

def get_gluten_badge(df=person_data_frame):
    items = gluten.get('terms')
    return apply_diet_filter(df, items)

def get_lectin_badge(df=person_data_frame):
    items = lectin.get('terms')
    return apply_diet_filter(df, items)

def get_lactose_badge(df=person_data_frame):
    items = lactose.get('terms')
    return apply_diet_filter(df, items)


#OUPUT

#get_user_stats

def print_df(df=person_data_frame):
    df_type = type(df)
    print(df_type)

def get_user_stats(df=person_data_frame):

    person = df.iloc[0, 0]
    entery_count = df.count()

    #.total_food_enteries = .entery_count.loc['trigger']
    total_food_enteries = len(df.trigger)

    total_symptom_enteries = len(df['symptom']!='NA') #????

    total_enteries = len(df)

    number_days_with_enteries = len(df.day.unique())

    first_entery = min(df['day'])

    last_entry = max(df['day'])

    rank = get_rank_badge

    complex_diet = get_complex_diet_badge

    archivist = get_archivist_badge

    coffee = get_coffee_badge
    gluten = get_gluten_badge
    lactose = get_lactose_badge
    lectin = get_lectin_badge


    table = {
        "User_ID": person,
        "tot_symp_stat": total_symptom_enteries,
        "tot_trig_stat": total_food_enteries,
        "tot_entery_stat": total_enteries,
        "first_entery": first_entery,
        "last_entery": last_entry,
        "rank_badge": get_rank_badge(),
        "complex_diet_badge": get_complex_diet_badge(),
        "archivist_badge": get_archivist_badge(),
        "coffee_badge": get_coffee_badge()
            }
    return pd.DataFrame.from_dict(table, orient='index') # or table





####RUNNING AREA




#print_csv(person_data_frame)

print_df()

print(get_user_stats())
