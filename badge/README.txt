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