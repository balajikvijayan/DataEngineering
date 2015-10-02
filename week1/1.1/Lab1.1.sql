1. select userid from events limit 10;
2. select userid, dt from users where campaign_id ='TW' limit 10;
3. select count(*) from users where campaign_id = 'FB';
4. select campaign_id,count(*) from users group by campaign_id;
5. select count(distinct dt) from users;
6. select max(dt) from users;
7. select min(dt) from users;
8. select avg(price) from meals;
9. select type, avg(price), min(price), max(price) from meals group by type;

10. select type, date_part('month', dt) as month, avg(price) avg_price, min(price) min_price, max(price) max_price from meals where (date_part('month', dt)<=3 and date_part('year',dt)=2013) group by type, month;

11. select meal_id, sum(case when event='bought' then 1 else 0 end) buys, SUM(CASE WHEN event='like' THEN 1 ELSE 0 END) likes, SUM(CASE WHEN event='share' THEN 1 ELSE 0 END)shares from events group by meal_id limit 10;

12. select type, avg(price) from meals group by type order by 2,1 desc;

13. select e.userid, u.campaign_id, e.meal_id, e.event from events e join users u on e.userid = u.userid limit 10;

14. select e.userid, u.campaign_id, e.meal_id, m.type, m.price from events e join users u on e.userid = u.userid join meals m on e.meal_id = m.meal_id and e.event = 'bought' limit 10;

15. select count(e.userid), m.type from events e join users u on e.userid = u.userid join meals m on e.meal_id = m.meal_id and e.event = 'bought' group by m.type limit 10;

16. select * from meals m where m.price > (select avg(price) from meals) limit 10;

17. select * from meals m where m.price > (select avg(m2.price) from meals m2 where m.type = m2.type) limit 10;

18. select count(m.meal_id), m.type from meals m where m.price > (select avg(m2.price) from meals m2 where m.type = m2.type) group by m.type limit 10;

19. select u.campaign_id, CAST(count(u.userid) AS REAL) from users u join users u2 on u.userid = u2.userid group by u.campaign_id

f
WITH u1 AS 
 (SELECT campaign_id, Count(*) AS n 
  FROM users
  GROUP BY campaign_id)
SELECT campaign_id, n, 
       (0.0+n)/(COUNT(*) OVER (PARTITION BY n))
FROM u1;

select campaign_id, COUNT(*) as campaigntotal, 
SUM(COUNT(*)) over() as total, 
(COUNT(*) * 1.0) / SUM(COUNT(*)) over() as percent
FROM users
group by campaign_id