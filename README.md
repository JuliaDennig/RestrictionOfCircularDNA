# Restriction of circular DNA

## What to use for?
The program searches for one/two enzyme(s) used in Restriction of circular DNA (plasmids).


## How to use?
You need the `.ape`-files with the sequence of the circular DNA. If the restriction enzyme should cut in a specific feature, the feature has to be marked in the `.ape` file. The results will be saved in a `.csv` file at a location of choice.
 
## Which enzymes are the program checking for?
You can find the list of enzymes and their features in the file `Enyzmes.csv`. The list can also be adapted to your needs.

## What are the criteria for suitable enzymes?
The restriction results in a minimum of three bands. All resulting bands are bigger than 300 bp. The difference between bands are at least 200 bp for bands smaller than 1000 bp, at least 300 bp for bands smaller than 3000 bp and at least 800 bp for bands bigger than 3000 bp.

## How do the single files of the program work together?
The file `OpenAPE.py` takes the location of the `.ape`-files, opens them and saves the features, their locations and the sequence.
The file `OpenEnzymeCSV.py` extracts the information about the enzymes from the given `Enzymes.csv`.
The file `FindBindingSites.py` takes the sequence from `OpenAPE.py` and the enzyme binding sequences from `OpenEnzymeCSV.py` and calculates the binding sites of the enzymes.
The file `CalculateBandSizes.py` calculates the band sizes of one/two enzymes based on the binding sites from `FindBindingSites.py`.
The file `FilterResults.py` filters the results meeting the criteria listed above, adds information in which features the chosen enzymes cut the cirular DNA and returns all results into a `.csv`-file at a location of choice.
