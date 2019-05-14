import sqlite3



""""
To start, I have 2 tables with 6 fields.
Data is time/date; string; oath thing; day; week; month
I basically want to do simple analysis.  Let me see if I can bring up my methods.
I want to figure out how many rows there are
I want to figure how many unique days have enteries.
I want to figure out the first entery
I also want to figure out the earliest (in the morning entry)
I want to count the uniqe food items

"""




#CONNECTION
conn = sqlite3.connect('db/user.db')
c = conn.cursor()




###########
# USER USE STATS
###########

def userUseStats():
    food_enteries = c.execute("SELECT COUNT(*) FROM tiggers;").fetchone()
    symptom_enteries = c.execute("SELECT COUNT(*) FROM symptoms;").fetchone()
    number_days_with_enteries = c.execute("SELECT COUNT(DISTINCT day) FROM symptoms;").fetchone()

    first_entery = c.execute(
    """
    SELECT MIN(day) FROM (SELECT DISTINCT day FROM symptoms.symptom
                        UNION ALL SELECT DISTINCT day FROM triggers.trigger)
    """ ).fetchone()


    last_entry = first_entery = c.execute(
    """
    SELECT MAX(day) FROM (SELECT DISTINCT day FROM symptoms.symptom
                        UNION ALL SELECT DISTINCT day FROM triggers.trigger)
    """ ).fetchone()

    total_enteries = food_enteries + symptom_enteries

    return {"food_enteries": food_enteries, "symptom_enteries": symptom_enteries,
            "number_days_with_enteries": number_days_with_enteries, "first_entery ": first_entery,
            "last_entry": last_entry, "total_enteries": total_enteries}

#DELETE PROBABLY first_entery = c.executemany("SELECT min(day) from triggers")





###################
# RANK : CITIZEN SCIENTIST
###################
# formula: number of enteries
# Newbie
def rankBadge():
    use_stats = userUseStats()
    total_enteries = use_stats[5]
    if total_enteries >= 10 and total_enteries < 15:
        return 1
    # Initiate Research
    elif total_enteries >= 15 and total_enteries < 25:
        return 2
    # Casual Researcher
    elif  total_enteries >= 25 and total_enteries < 50:
        return 3
    # Research Enthusiast
    elif  total_enteries >= 50 and total_enteries < 100:
        return 4
    # Scholar
    elif  total_enteries >= 100 and total_enteries < 200:
        return 5
    # Master Researcher
    elif  total_enteries >= 200:
        return 6
    else:
        return 0
############
# MISC_badge
############

#WORKING
# of foods using unique count?

