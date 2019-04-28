from badgeModule import Badge, prepare_csv
from pathlib import Path
import pprint
import pandas as pd

#badgeModule, runner.py, and test_badge should all be in the same directory.
#Enter the csv paths.



#Enter Symptom Path
sympPath =  Path('C:/webDev/pycharm/dieta/data/ak_symptoms.csv')
#Enter Trigger Path
trigPath =  Path('C:/webDev/pycharm/dieta/data/ak_triggers.csv')

### RUNNING SPACE ###
combined_csv = prepare_csv(sympPath, trigPath)

asaf = Badge(1, combined_csv)
asaf.get_user_stats()
print('USER STATS **************')
pprint.pprint(asaf.show_user_stats_dict())
print('*************************')

print('Citizen Scientist Badge Level:' + str(asaf.get_rank_badge()))

print('Complex Badge: ' + str(asaf.get_complex_diet_badge()))
print('Archivist Badge; ' + str(asaf.get_archivist_badge()))
print('Coffee Badge; ' + str(asaf.get_coffee_badge()))
print('Lactose Badge: ' + str(asaf.get_lactose_badge()))
print('*********USER STATS AND BAGES***********')
pprint.pprint(asaf.create_table())

#You Can Output to CSV
#asaf.output_to_csv()

