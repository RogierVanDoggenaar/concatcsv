# Concatenate CSV files

### usage:
run the python script with all input files that need to be concatenated as arguments. The last argument should be the 
name of the resulting outputfile. 
```bash
python -m concatcsv 'sample-1.csv' 'sample-2.csv' 'sample-3.csv' 'output.csv' 
```

> *Note:* All files are expected to have the fiefld names in the first line, therefore only the first line of the first 
> file will be added to the output. All other files will be added from line 2 onward.