import psycopg2

q1 = '''select articles.title,popular_articles.views as number_of_view 
from articles,popular_articles
where '/article/' || articles.slug = popular_articles.path
limit 3;'''
q2 = '''select authors.name,count(log.path) as number_of_view from authors,log,articles
where '/article/' || articles.slug = log.path and articles.author = authors.id
group by authors.name
order by number_of_view desc;'''
q3 = '''select to_char(num_of_success_by_day.date,'Month dd yyyy'), round(num_of_error_by_day.numOfError*100.0/
num_of_success_by_day.numOfSuccess,2)as percentage_of_errors
from num_of_success_by_day,num_of_error_by_day
where ((Cast (num_of_error_by_day.numOfError as float)/cast(num_of_success_by_day.numOfSuccess as float))>=0.01 and 
num_of_success_by_day.date = num_of_error_by_day.date);'''


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

