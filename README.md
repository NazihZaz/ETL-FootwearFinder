# Project2-ETL-FootwearFinder

Project 2 Proposal – Extract, Transform, Load (ETL) - GATECH Data Science and Analytics Bootcamp.

The purpose of this project is to demonstrate our ability to perfom the ETL process using Jupyter Notebooks, pgAdmin 4, Pandas, Python, and many other libraries available to us.

## Team Name:  
The Footwear Finder.

## Team Members:
• Bouanani, Nazih

• Purwanto, Ellis

• Wamulanga, Arnold 

## Topic: eCommerce footwear industry.

### Description: 
Develop a database of footwear retail data from one or multiple sources listed below to include product and price information and load them to a database to be used for further market analysis. 

## Sources:
• Kaggle

• API from www.shop.com

• www.nike.com

## Steps:
1. Extract: The data was pulled from 2 different sources using 2 different methods.

	a) API Calls from www.shop.com. [Click here to access Jupyter Notebook for API Calls](https://github.com/epurwant0/Project2-ETL-FootwearFinder/blob/main/Footwear%20Finder.ipynb)

	b) Websraping on www.nike.com. [Click here to access Jupyter Notebook for Websraping](https://github.com/epurwant0/Project2-ETL-FootwearFinder/blob/main/nike_ETL.ipynb)

2. Transform: After extracting the data, we saved the data into Pandas data frames and cleaned our data (i.e.: parse through strings, convert prices to decimals, etc...)

3. Load:

	a) Create a database named FootwearFinder_db using pgAdmin 4.

	b) Create a table named ["shoes"](https://github.com/epurwant0/Project2-ETL-FootwearFinder/blob/main/schema.sql).

	c) Import csv files to our 3rd [Jupyter Notebook](https://github.com/epurwant0/Project2-ETL-FootwearFinder/blob/main/SCAthletic_etl.ipynb), turn them into Pandas data frames, create a connection to the database, load both data frames, and laslty make a query to confirm that everything was loaded.

As a bonus part, we have done some web visualtion using [Flask](https://github.com/epurwant0/Project2-ETL-FootwearFinder/blob/main/app.py) and [HTML](https://github.com/epurwant0/Project2-ETL-FootwearFinder/blob/main/templates/index.html) using render_template and displayed the data (Local Development).