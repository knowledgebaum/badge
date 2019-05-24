from pathlib import Path
import pandas as pd
import numpy as np
import os.path



####################
#DATA/CSV PREP
####################


def prepare_csv(csv1, csv2):
    sympPath = csv1
    trigPath = csv2
    symp_df = pd.read_csv(sympPath)
    trig_df = pd.read_csv(trigPath)
    #symptom_enteries = symp_df
    #food_enteries = trig_df
    #dataFrame = pd.concat([symp_df, trig_df], axis=0, ignore_index=True, sort=False)
    dataFrame = pd.merge(symp_df, trig_df, how='outer')
    #dataFrame = pd.merge(symp_df, trig_df, how='outer')

    dataFrame['day'] = pd.to_datetime(dataFrame['day'])
    dataFrame['ts'] = pd.to_datetime(dataFrame['ts']) #may break

    # #ERROR TESTING
    # if os.path.basename(sympPath) and os.path.basename(trigPath):
    #     raise NameError('The files are not CSVs')
    # if os.path.exists(sympPath) and os.path.exists(trigPath):
    #     raise NameError('The path to one of your CSV files is wrong.')
    return dataFrame




class Badge():

    def __init__(self, userID, csv):
        self.userID = userID


        #LOAD DATA From Data CSV for testing
        self.data = csv


        #DIET CATEGORYS DICTIONARYS
        self.coffee = {'category': 'coffee', 'terms': ['coffee', 'latte', 'americano', 'espresso',
                                                        'breve', 'cappucino', 'mocha', 'macchiato']}
        self.gluten = {'category': 'gluten', 'terms': ['bread', 'pasta', 'sour dough', 'macaroni', 'wheat', 'gnocchi',
                                                        'pretzels', 'pancakes', 'waffles', 'biscuits']}
        self.lactose = {'category': 'lactose', 'terms': ['milk', 'cheese', 'yogurt', 'alfredo']}
        self.lectin = {'category': 'lectin', 'terms': ['potato', 'tomato', ]}



####################
# STAT FUNCTIONS
####################

    # USER USE STATS
    def get_user_stats(self):
        self.entery_count = self.data.count()

        #self.total_food_enteries = self.entery_count.loc['trigger']
        self.total_food_enteries = len(self.data.trigger)

        self.total_symptom_enteries = self.entery_count.loc['symptom']

        self.total_enteries = len(self.data)

        self.number_days_with_enteries = len(self.data.day.unique())

        self.first_entery = min(self.data['day'])

        self.last_entry = max(self.data['day'])


####################
#RANK :CITIZEN SCIENTIST
####################

    def get_rank_badge(self):

        total_enteries = self.total_enteries

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


####################
# MISC BADGES
####################

    ##COMPLEX DIET BADGE

    def get_complex_diet_badge(self):

        COMPLEX_DIET_VAL = 50

        # print(trig_df.head()) Just seeing if everything worked
        complexDiet = self.data['trigger'].count()  # changed from nunique

        if complexDiet > COMPLEX_DIET_VAL:
            return True
        else:
            return False

    ##ARCHIVIST BADGE
    def get_archivist_badge(self):

        ARCHIVIST_VAL = 20

        max_enteries_per_day = self.data.groupby(['day'])[['symptom', 'trigger']].count()

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
    def apply_diet_filter(self, diet):

        self.data['trigger'] = self.data['trigger'].str.lower()
        filter = self.data['trigger'].isin(diet)
        category_count = len(self.data[filter])

        if category_count > 0:
            return True
        else:
            return False

    def get_coffee_badge(self):
        items = self.coffee.get('terms')
        return self.apply_diet_filter(items)


    def get_gluten_badge(self):
        items = self.gluten.get('terms')
        return self.apply_diet_filter(items)

    def get_lectin_badge(self):
        items = self.lectin.get('terms')
        return self.apply_diet_filter(items)

    def get_lactose_badge(self):
        items = self.lactose.get('terms')
        return self.apply_diet_filter(items)


####################
#OUTPUT DATA
####################

    def show_user_stats_dict(self):
        return {
                "total_food_enteries": self.total_food_enteries,
                "total_symptom_enteries": self.total_symptom_enteries,
                "total_enteries": self.total_enteries,
                "number_days_with_enteries": self.number_days_with_enteries,
                "first_entery ": self.first_entery,
                "last_entry": self.last_entry
                }


    def create_table(self):

        table = {
            "PK_ID": [1],
            "User_ID": ["Asaf"],
            "tot_symp_stat": self.total_symptom_enteries,
            "tot_trig_stat": self.total_food_enteries,
            "tot_entery_stat": self.total_enteries,
            "first_entery": self.first_entery,
            "last_entery": self.last_entry,
            "rank_badge": self.get_rank_badge(),
            "complex_diet_badge": self.get_complex_diet_badge(),
            "archivist_badge": self.get_archivist_badge(),
            "coffee_badge": self.get_coffee_badge()
                }
        return table


    def output_to_csv(self, output_path=None):
        if output_path == None:
            csv_output_path = Path('C:\webDev\pycharm\dieta\data\export_badges.csv')
        else:
            csv_output_path = Path(output_path)
        table = self.create_table()
        df = pd.DataFrame(data=table)
        df.to_csv(csv_output_path)
        # https://datatofish.com/export-dataframe-to-csv/

    # To Database output
    def output_to_db(self, badge_table):
        table = self.create_table()
        pass
        # Add to database here
        #


####################
#LOAD DATA
####################

    def get_badges_from_database(self, badge_table):
        """Loads data from the Badge Table"""
        """TO DEVELOP LATER"""
        print('This will display all the badges from a table')
        pass



####################
#####CUT OUT / EXCISE
####################
##
        ##TOP 10 COFFEE WORDS  :>OBJECT that is food :>Dairy, Gluten,
        ##make variables which are top 10 of each food category
        ##
        # test_count = (trig_df['trigger'].str.contains('Coffee')) & (trig_df['trigger'].str.contains('coffee')).sum()

        # lower case column
        #
        # coffee_filter = self.data['trigger'].str.lower().isin(['coffee', 'latte', 'americano', 'espresso',
        #                                                        'breve', 'cappucino', 'mocha', 'macchiato'])


##Coffee Badge

# def get_coffee_badge(self):
#
#     ## MULTIPLE DATA
#     ##https://www.geeksforgeeks.org/python-pandas-dataframe-isin/
#
#     coffee_count = self.data['trigger'].str.contains('Coffee').sum() + self.data['trigger'].str.contains(
#         'coffee').sum()  # or any()
#
#
#
#     if coffee_count > 0:
#         return True
#     else:
#         return False

##########
##Testing
##diet category
##########




       ###VERBOSE VERSION
    # coffee_filter = self.data['trigger'].isin([coffee])
    # gluten_filter = self.data['trigger'].isin([gluten])
    # lactose_filter = self.data['trigger'].isin([lactose])
    # lectin_filter = self.data['trigger'].isin([lectin])
    #
    # len(self.data[coffee_filter])
    # len(self.data[gluten_filter])
    # len(self.data[lactose_filter])
    # len(self.data[lectin_filter])
