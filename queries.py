#!/usr/bin/env python3

import psycopg2

q1 = '''SELECT  articles.title,popular_articles.views AS number_of_view 
FROM articles,popular_articles
WHERE '/article/' || articles.slug = popular_articles.path
LIMIT 3;'''
q2 = '''SELECT authors.name,SUM(popular_articles.views) AS number_of_view
FROM authors,popular_articles,articles
WHERE '/article/' || articles.slug = popular_articles.path 
AND articles.author = authors.id
GROUP BY authors.name
ORDER BY number_of_view desc;'''
q3 = '''SELECT to_char(num_of_success_by_day.date,'FMMonth dd yyyy'), round(num_of_error_by_day.numOfError*100.0/
(num_of_success_by_day.numOfSuccess + num_of_error_by_day.numOfError),2) AS percentage_ofS_errors
FROM num_of_success_by_day,num_of_error_by_day
WHERE (num_of_error_by_day.numOfError::float /(num_of_success_by_day.numOfSuccess + num_of_error_by_day.numOfError)::float)>=0.01 AND 
(num_of_success_by_day.date = num_of_error_by_day.date);'''


db = psycopg2.connect("dbname=news")
cursor = db.cursor()

print("1. What are the most popular three articles of all time?\n")
cursor.execute(q1)
answer1 = cursor.fetchall()
for i in range(0, len(answer1)):
    print("\t\"%s\" — %d views" % answer1[i])
print("\n")

print("2. Who are the most popular article authors of all time?\n")
cursor.execute(q2)
answer2 = cursor.fetchall()
for i in range(0, len(answer2)):
    print("\t%s — %d views" % answer2[i])
print("\n")

print("3. On which days did more than 1% of requests lead to errors?\n")
cursor.execute(q3)
answer3 = cursor.fetchall()
for i in range(0, len(answer3)):
    print("\t%s — %.2f%% error" % answer3[i])
print("\n")

db.close()

