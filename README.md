#Simple Badges

## Getting Started
Clone the repository.  Go into the badge folder. Run simple_badge_module with the argument 1 or 2 ( where 1 = AK, 2 = TA).

__UPDATING IN PROGRESS__


# Badges

This project aims to gamify the Dieta app by providing users badges for certain thresholds achieved when recording  their user data.
It takes input data from Dieta and outputs user stats, and various badges based on diet, 
(like how frequently users add 
information to the app, and the total number of enteries users have made.)

## Getting Started
Clone the repository.  Go into the badge folder.  Run runner.py to demo the badgeModule (which contains the Badge class) on the provided data.  (You will have to change the sympPath and trigPath to the correct path for ak_symptoms, ak_triggers for your system file structure. )

### To use the badgeModule 

 
Import badgeModule, pathlib, pprint

1. prepare data csv files using prepare_csv()
2. create named instance with Badge()  
3. print user stats and badges using the Badge class methods


Example
```
combined_csv = prepare_csv(sympPath, trigPath)
asaf = Badge(1, combined_csv)
asaf.get_user_stats()

print('Complex Badge: ' + str(asaf.get_complex_diet_badge()))


```

Note:
The first argument for badge doesn't matter at the moment.  It is designed for a future version in mind.

### Prerequisites


The application requires the 2 CSVs in the **data folder** PANDAS, Path (from Pathlib) and Python.  


```
ak_symptoms.csv
ak_triggers.csv
```
<!--
### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo
-->

## Running the tests

<!--Explain how to run the automated tests for this system -->

Run the Test_Badge.py to test the provided data.


### Tests in Test_Badge do


Test provided data 
1. Test ******
2. Rank of provided data is 6
3. Complex Data Badge is true
4. Archivist Badge is true 
5. Coffee Badge is true
6. Rank Badge of create_table() is 6

