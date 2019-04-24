from .badge import Badge, prepare_csv
from pathlib import Path

### RUNNING SPACE ###

sympPath =  Path('C:/webDev/pycharm/dieta/data/ak_symptoms.csv')
trigPath =  Path('C:/webDev/pycharm/dieta/data/ak_triggers.csv')
combined_csv = prepare_csv(sympPath, trigPath)


asaf = Badge(1, combined_csv)
print(asaf.get_user_stats())
print(asaf.show_user_stats_dict())

print(asaf.get_rank_badge())

print(asaf.get_complex_diet_badge())
print(asaf.get_archivist_badge())
print(asaf.get_coffee_badge())
print(asaf.create_table())