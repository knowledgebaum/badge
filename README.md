# badge

""""# CLASS VERSION

Consumes a userID and a data source.  The class only handles csv but was designed to be extended to handle database connections.

After the data is loaded, the get_user_stats method calculates user stats and sets them as attribute variables (e.g. number of food enteries, symptom enteries, total enteries, first entry, last entry).

Show_user_Stats_dict produces a dictionary of user stats.

The next section of the code calculates badges earned by the user.

The get_rank_badge() method determines what level (rank) of badge the user has earned in the citizen scientist rank.  This badge correlates with the rank badge screen of the user stats area.  The rank is calculated by the number user enteries into the Dieta diary (e.g triggers, symptoms, etc.).  The more enteries the higher the rank.

The get_complex_diet_badge() method returns a True/False value if the complex diet achievement has been earned.  The badge is dependent on the number of unique trigger items recorded.

The get_archivist_badge method returns a True/False value to determine if the archivist achievement has been earned.  The method calculates the maximum number of diary enteries in a single day.  Users who hit a certain amount of enteries in a single day earn this badge.

The get_coffee_badge returns a True/ False depending on the number of times a user has recorded coffee in the Dieta diary ( trigger colummn).


The output section contains 3 methods.  The badge information can be output to the console (in a dataframe), a CSV, or to an external database.

The create_table() method will create a table (in PANDAS dataframe) from the values above.

To Build (below):
The output_to_csv method will output the table to a csv file.

The output_to_db method will output the table to a database.

The load section, specifically get_badges_from_table() deals with loading badges from an external badge table.  Some badges don't need to be recalculated.  The badge/ user stats area of the Dieta app can load pre calculated badges from the badge table.

"""
