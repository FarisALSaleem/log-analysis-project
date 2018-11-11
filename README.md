Introduction
----------------------------------------------------------------------------------------------------
This repository contains python3 code and two text files for the log-analysis-project from udacity.

How-to-run
----------------------------------------------------------------------------------------------------
1-make sure that you have psycopg2 installed.
Note: install psycopg2-binary if you don't want the random User warnings.
2-make sure that you create the views in the views.txt file.
3-run queries.py in the command line or terminal.

Note: This code was written for python3 and will not work for python2.

Description
----------------------------------------------------------------------------------------------------
This program connects the news database that is given in the project and performs queries to 
answer the following questions:

1- What are the most popular three articles of all time? 
2- Who are the most popular article authors of all time? 
3- On which days did more than 1% of requests lead to errors?

View
----------------------------------------------------------------------------------------------------
these are the views that need to be created before running queries.py.

create view num_of_error_by_day as 
select date(time) as date,count(status) as numOfError 
from log 
where(status like '4__%' or status like '5__%')group by date order by date;

create view num_of_success_by_day as 
select date(time) as date,count(status) as numOfSuccess
from log 
where not(status like '4__%' or status like '5__%')group by date order by date;

create view popular_articles as 
select path,count(*) as views 
from log group by path
order by views desc;

Output example
----------------------------------------------------------------------------------------------------
1. What are the most popular three articles of all time?

        "Candidate is jerk, alleges rival" — 338647 views
        "Bears love berries, alleges bear" — 253801 views
        "Bad things gone, say good people" — 170098 views


2. Who are the most popular article authors of all time?

        Ursula La Multa — 507594 views
        Rudolf von Treppenwitz — 423457 views
        Anonymous Contributor — 170098 views
        Markoff Chaney — 84557 views


3. On which days did more than 1% of requests lead to errors?

        July      17 2016 — 2.32% error

Repository contains
----------------------------------------------------------------------------------------------------
queries.py -contains python3 code that performs queries on the news database.
views.text -contains the views statements that need to be created for the code to work.
queries.text -sql statements that are used in queries.py(not need for the code to work). 
 