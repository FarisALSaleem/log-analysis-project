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
