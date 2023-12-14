# Welcome to My Ds Babel
***

## Task
The task here was to convert SQL and CSV datasets to CSV and SQL datasets, respectively. 

## Description
The problem of converting SQL to CSV was solved by using python's sqlite3 to connect to a 
database, converting the data table to a pandas dataframe, and then using pandas' to_csv()
function to return a csv string. The problem of converting CSV to SQL was solved by converting
theh csv to a pandas dataframe and then using pandas' to_sql function to save the data to a 
database. 

## Installation
A Python installation with the following packages is required:
sqlite3, pandas, csv, and io. 

## Usage
Tests are included in the main function. The datasets will need to be downloaded 
via the command 

wget <link> 

for https://storage.googleapis.com/qwasar-public/track-ds/list_volcano.csv and 
https://storage.googleapis.com/qwasar-public/track-ds/all_fault_line.db

### The Core Team
Completed by Andrew Bonham and Nikita Gaidamachenko. 

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
