



from pathlib import Path
import pandas as pd
import numpy as np


########
#Data Prep for Badge
########



def prepare_csv(csv1, csv2):
    sympPath = csv1
    trigPath = csv2
    symp_df = pd.read_csv(sympPath)
    trig_df = pd.read_csv(trigPath)
    #symptom_enteries = symp_df
    #food_enteries = trig_df
    dataFrame = pd.concat([symp_df, trig_df], sort=False)
    dataFrame['day'] = pd.to_datetime(dataFrame['day'])
    dataFrame['ts'] = pd.to_datetime(dataFrame['ts']) #may break

    return dataFrame




class Badge():

    def __init__(self, userID, csv):
        self.userID = userID
        ##LOAD DATA## # From Data CSV for testing
        self.data = csv




    # stat function
    ###########
    # USER USE STATS
    ###########
    def get_user_stats(self):
        self.entery_count = self.data.count()

        self.total_food_enteries = self.entery_count.loc['trigger']

        self.total_symptom_enteries = self.entery_count.loc['symptom']

        self.total_enteries = len(self.data)

        self.number_days_with_enteries = len(self.data.day.unique())

        self.first_entery = min(self.data['day'])

        self.last_entry = max(self.data['day'])

    def show_user_stats_dict(self):
        return {
                "total_food_enteries": self.total_food_enteries,
                "total_symptom_enteries": self.total_symptom_enteries,
                "total_enteries": self.total_enteries,
                "number_days_with_enteries": self.number_days_with_enteries,
                "first_entery ": self.first_entery,
                "last_entry": self.last_entry
                }




    # attribute badges

    # get badges

    ###################
    # RANK : CITIZEN SCIENTIST
    ###################
    # formula: number of enteries
    # Newbie

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

    ############
    # MISC BADGES
    ###########

    ##COMPLEX DIET

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

            ##Coffee Badge

    def get_coffee_badge(self):

        coffee_count = self.data['trigger'].str.contains('Coffee').sum() + self.data['trigger'].str.contains(
            'coffee').sum()  # or any()
        ##
        ##TOP 10 COFFEE WORDS  :>OBJECT that is food :>Dairy, Gluten,
        ##make variables which are top 10 of each food category
        ##
        # test_count = (trig_df['trigger'].str.contains('Coffee')) & (trig_df['trigger'].str.contains('coffee')).sum()

        if coffee_count > 0:
            return True
        else:
            return False

    ############
    # load badges from DB
    ############
    def get_badges_from_table(self, badgeTableConnection):
        print('This will display all the badges from a table')

    ##########
    # output
    ##########

    # To Data Frame Method
    def create_table(self):

        table = pd.DataFrame({
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
            "coffee_badge": self.get_coffee_badge()},
            index=[1]
        )

    def output_to_csv(self):
        table = self.create_table()
        table.to_csv(r'C:\webDev\pycharm\dieta\data\export_badges.csv')
        # https://datatofish.com/export-dataframe-to-csv/

    # To Database output
    def output_to_db(self):
        table = self.create_table()
        # Add to database here
        #
        #
        #

    # Not written


#LOAD DATA







