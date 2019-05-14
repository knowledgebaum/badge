from datetime import datetime, timedelta
from hashlib import md5
from time import time
from flask import current_app, url_for
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

from app import db
from application import db, login
import json
from time import time
import base64
import os

table = ''

class Badge(table):
   def __init__(self, path):

    self.table = path





###########
# STATS
###########

    food_enteries = "select * from triggers"
    symptom_enteries = "select * from symptoms"
    days_with_enteries = len(table.column("day").unique)  ##NOT THERE YET
    First_entery = "select min(Day) from triggers"

    total_enteries = food_enteries + symptom_enteries



    ##NEED counts
###################
# citizen_scientist RANK
###################
    # formula: number of enteries

    # Newbie
    if total_enteries >= 100 and total_enteries < 1000:

    # Initiate Research
    else if total_enteries >= 1000 and total_enteries < 10000:

    # Casual Researcher
    else if total_enteries >= 1000 and total_enteries < 10000:

    # Research Enthusiast
    else if total_enteries >= 1000 and total_enteries < 10000:

    # Scholar
    else if total_enteries >= 1000 and total_enteries < 10000:

    # Master Researcher
    else if total_enteries >= 1000 and total_enteries < 10000:

############
# MISC_badge
############
    # Morning

    # Night

    # Complex Diet
    # of foods using unique count?
        days_with_enteries = len(table.column("tiggers").unique)  ##NOT THERE YET
    # one day@ a time

    # archivist
    # 20 enteries in 1 day
        "from count column where day = __some Number__"

    # weekend
    # recorded on the week end
        "check to see if day is in weekend"
        df['day'] = df['day'].dt.weekdayName
        df['weekend'] =np.where(df['day']=='Saturday', 'yes', 'no')

#########
# streaks
#########
    # Recorded 2 days in a row

    # Recorded 3 Days in a row

    # Recorded 7 days in a row

    # recorded 2 weeks in a row

###ORM###
"""
class Badge(db.Model):
    id = db.Column(db.Integer, pr)

"""

obj = Badge()

