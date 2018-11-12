#!/usr/bin/env python3

import psycopg2


def db_connect():
    """
    Creates and returns a connection to the database defined by DBNAME,
    as well as a cursor for the database.
    Returns:
        db, c - a tuple. The first element is a connection to the database.
                The second element is a cursor for the database.
    """
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    return (db, cursor)


def execute_query(query):
    """
    execute_query takes an SQL query as a parameter.
    Executes the query and returns the results as a list of tuples.
    args:
    query - an SQL query statement to be executed.

    returns:
    A list of tuples containing the results of the query.
    """
    db = db_connect()
    db[1].execute(query)
    result = db[1].fetchall()
    db[0].close()
    return result


def print_top_articles():
    """Prints out the top 3 articles of all time."""
    query = '''SELECT  articles.title,popular_articles.views AS number_of_view
    FROM articles,popular_articles
    WHERE '/article/' || articles.slug = popular_articles.path
    LIMIT 3;'''
    results = execute_query(query)

    print("1. What are the most popular three articles of all time?\n")
    for title, view in results:
        print('\t"{}" — {} views'.format(title, view))
    print("\n")


def print_top_authors():
    """Prints a list of authors ranked by article views."""
    query = '''SELECT authors.name,SUM(popular_articles.views)
    AS number_of_view
    FROM authors,popular_articles,articles
    WHERE '/article/' || articles.slug = popular_articles.path
    AND articles.author = authors.id
    GROUP BY authors.name
    ORDER BY number_of_view desc;'''
    results = execute_query(query)

    print("2. Who are the most popular article authors of all time?\n")
    for author, view in results:
        print("\t{} — {} views".format(author, view))
    print("\n")


def print_errors_over_one():
    """
        Prints out the days where more than 1% of
        logged access requests were errors.
    """
    query = '''SELECT to_char(num_of_success_by_day.date,'FMMonth dd yyyy'),
    round(num_of_error_by_day.numOfError*100.0/
    (num_of_success_by_day.numOfSuccess + num_of_error_by_day.numOfError),2)
    AS percentage_ofS_errors
    FROM num_of_success_by_day,num_of_error_by_day
    WHERE (num_of_error_by_day.numOfError::float /
    (num_of_success_by_day.numOfSuccess + num_of_error_by_day.numOfError)::
    float)>=0.01
    AND (num_of_success_by_day.date = num_of_error_by_day.date);'''
    results = execute_query(query)

    print("3. On which days did more than 1% of requests lead to errors?\n")

    for date, percent in results:
        print("\t{} — {} error".format(date, percent))
    print("\n")


if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_errors_over_one()
