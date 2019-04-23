""""# CLASS VERSION

Consumes a userID and an optional data source.  If no data source is provided the data variable is a couple of csvs.

After the data is loaded, the get_user_stats method calculates user stats (e.g. number of food enteries, symptom enteries, total enteries, first entry, last entry).

The userStats attribute is set using this method.


The next section of the code calculates badges earned by the user.

The get_rank_badge() method determines what level (rank) of badge the user has earned in the citizen scientist rank.  This badge correlates with the rank badge screen of the user stats area.  The rank is calculated by the number user enteries into the Dieta diary (e.g triggers, symptoms, etc.).  The more enteries the higher the rank.

The get_complex_diet_badge() method returns a True/False value if the complex diet achievement has been earned.  The badge is dependent on the number of unique trigger items recorded.

The get_archivist_badge method returns a True/False value to determine if the archivist achievement has been earned.  The method calculates the maximum number of diary enteries in a single day.  Users who hit a certain amount of enteries in a single day earn this badge.

The get_coffee_badge returns a True/ False depending on the number of times a user has recorded coffee in the Dieta diary ( trigger colummn).

The next section deals with loading badges from an external badge table.  Some badges don't need to be recalculated.  The badge/ user stats area of the Dieta app can load pre calculated badges from the badge table.

-----
conjecture
-----
this method can consume


The output section contains 3 methods.  The badge information can be output to the console (in a dataframe), a CSV, or to an external database.

The create_table() method will create a table from the values above.
The output_to_csv method will output the table to a csv file.
The output_to_db method will output the table to a database. """



from pathlib import Path
import pandas as pd
import numpy as np


class Badge():

    def __init__(self, userID, csv, database=None)
        self.userID = userID

        ##LOAD DATA##
        # From Database
        if data is not None:
            self.data = data
        # From Data CSV for testing
        else:
            symp_df = pd.read_csv(sympPath)
            trig_df = pd.read_csv(trigPath)
            # symptom_enteries = symp_df
            # food_enteries = trig_df
            all_enteries = pd.concat([symp_df, trig_df], sort=False)
            all_enteries['day'] = pd.to_datetime(all_enteries['day'])
            all_enteries['ts'] = pd.to_datetime(all_enteries['ts'])  # may break

            self.data = all_enteries

    # stat function
    ###########
    # USER USE STATS
    ###########
    def get_user_stats(self):

        total_food_enteries = len(self.data['trigger'])

        total_symptom_enteries = len(all_enteries['symptom'])

        total_enteries = len(all_enteries)

        number_days_with_enteries = len(all_enteries.day.unique())

        first_entery = min(all_enteries['day'])

        last_entry = max(all_enteries['day'])

        return {"total_food_enteries": total_food_enteries, "total_symptom_enteries": total_symptom_enteries,
                "number_days_with_enteries": number_days_with_enteries, "first_entery ": first_entery,
                "last_entry": last_entry, "total_enteries": total_enteries}

    ###SET USER STATS attribute
    self.user_stats = get_user_stats():

    def display_user_stats(self):
        for i in self.user_stats.items():
            print(i)

    # attribute badges

    # get badges

    ###################
    # RANK : CITIZEN SCIENTIST
    ###################
    # formula: number of enteries
    # Newbie

    def get_rank_badge(stats=self.userStats):

        use_stats = userStats
        total_enteries = use_stats.get('total_enteries')

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
        complexDiet = all_enteries['trigger'].count()  # changed from nunique

        if complexDiet > COMPLEX_DIET_VAL:
            return True
        else:
            return False

    ##ARCHIVIST BADGE
    def get_archivist_badge(self):

        ARCHIVIST_VAL = 20

        max_enteries_per_day = all_enteries.groupby(['day'])[['symptom', 'trigger']].count()

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

        coffee_count = all_enteries['trigger'].str.contains('Coffee').sum() + all_enteries['trigger'].str.contains(
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
    def create_table():
        stats = self.userStats

        table = pd.DataFrame({
            "PK_ID": [1],
            "User_ID": ["Asaf"],
            "tot_symp_stat": stats.get('total_symptom_enteries'),
            "tot_trig_stat": stats.get('total_food_enteries'),
            "tot_entery_stat": stats.get('total_enteries'),
            "first_entery": stats.get('first_entery'),
            "last_entery": stats.get('last_entry'),
            "rank_badge": rankBadge(),
            "complex_diet_badge": complexDietBadge(),
            "archivist_badge": archivistBadge(),
            "coffee_badge": coffeeBadge()},
            index=[1]
        )

    def output_to_csv:
        table = create_table()
        table.to_csv(r'C:\webDev\pycharm\dieta\data\export_badges.csv')
        # https://datatofish.com/export-dataframe-to-csv/

    # To Database output
    def output_to_db():
        table = create_table()
        # Add to database here
        #
        #
        #

    # Not written


#LOAD DATA

sympPath =  Path('C:/webDev/pycharm/dieta/data/ak_symptoms.csv')
trigPath =  Path('C:/webDev/pycharm/dieta/data/ak_triggers.csv')


def prepare_csv():
    symp_df = pd.read_csv(sympPath)
    trig_df = pd.read_csv(trigPath)
    #symptom_enteries = symp_df
    #food_enteries = trig_df
    all_enteries = pd.concat([symp_df, trig_df], sort=False)
    all_enteries['day'] = pd.to_datetime(all_enteries['day'])
    all_enteries['ts'] = pd.to_datetime(all_enteries['ts']) #may break

asaf = Badge(1)
print(asaf.get_user_stats())
print(asaf.user_stats())

print(asaf.get_rank_badge())

print(get_complex_diet_badge)
print(get_archivist_badge)
print(get_coffee_badge)
print(create_table())