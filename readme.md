## Introduction

This is my solution to the technical challenge sent to me yesterday. Please find instructions 
on how to setup and test the solution

## Setup 
Please create and activate virtual environment in  the project folder and run the following command to install the requirments 

> pip install -r requirments.txt

## Project structure
There are 3 folders in the project folder 
1. Data -- contains the copy of the uniprot sequences csv file, and a sample test_csv for unit testing  

2. Src -- The src folder contains in it the actual code solution to the task given  

3. Tests -- This contains the unit tests cases for the solution  

### Testing the project 
You can run the code from the root of the folder with 
>python src/index.py 

The code will execute, extract the features  and save it into  a csv file by name `processed_data.csv`

### Runing the unit test cases 

The unit test is setup with pytest 
By running `pytest` in the root folder, the test cases will run 