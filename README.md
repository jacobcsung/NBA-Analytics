# nba-analytics

## About 
Simply a personal project, will solely be used for educational purposes. Provided an opportunity to learn webscraping with Python, data manipulation with Pandas, Python and SQLite interactions, database normalization/management, and statistical analysis of real world data. 

## Lightweight Webscraper
Heavily using the ```Requests``` module from Python, this simple webscraper is a tool that (respectfully) scrapes datasets from the NBA's offical statpage. The tool allows the ability to specify season years as well as the type of data requested by only changing HTML headers and specific URLs. Data is collected and then exported to CSV files using built-in Pandas helper methods.

## Simple SQLite Database
A Simple SQLite database for storage of scraped data. Useful for querying specific subsets of data for purposes of analysis. Database is structured to meet 2NF standards. Prior to storage, data had been cleaned and reorganized using Excel and Pandas DF manipulation methods.

## Analytics (IN PROGRESS)
