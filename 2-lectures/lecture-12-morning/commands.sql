SHOW TABLES;

DESCRIBE country;

-- SELECT

SELECT * FROM country;

SELECT Name, countryCode from city;

-- WHERE

SELECT Name, Code FROM country WHERE Continent = "North America";

SELECT Name FROM country WHERE Continent = "Asia" AND Population > 100000000;

-- WHERE with IN operator

SELECT Name, Population FROM country WHERE (Continent IN ("Asia", "Europe") OR Name = "United States") AND Population > 50000000;

-- ORDER BY

SELECT Name, Population FROM country ORDER BY Population ASC;

SELECT Name, Population FROM country ORDER BY Population DESC;

-- LIMIT

SELECT Name, Population FROM country ORDER BY Population DESC LIMIT 5;

SELECT Name, Population FROM city ORDER BY Population DESC LIMIT 5;


-- UNION
SELECT Name, Population FROM country 
UNION
SELECT Name, Population FROM city ORDER BY Population DESC;

-- WHERE with LIKE

SELECT Name, Population FROM country WHERE Name LIKE "%Sudan%";

-- INSERT

INSERT INTO country(Code, Name, IndepYear)
VALUES ("SS", "South Sudan", 2011);

SELECT Name, Population FROM country WHERE Name LIKE "%Sudan%";

-- DELETE

DELETE FROM country WHERE Name = "South Sudan";

-- COUNT(*)

SELECT count(*) AS num_countries from country;

-- COUNT + filtering

SELECT count(*) AS num_big_countries
FROM country WHERE population >= 50000000;

-- BETWEEN

SELECT count(*) AS num_medium_countries FROM country
WHERE population BETWEEN 25000000 AND 50000000;

-- GROUP BY

SELECT countrycode, count(ID) AS num_cities, SUM(Population) AS
  city_total_population FROM city GROUP BY CountryCode LIMIT 4;


-- GROUP BY + ORDER

SELECT countrycode, count(ID) AS num_cities, SUM(Population) AS
  city_total_population FROM city GROUP BY CountryCode
  ORDER BY city_total_population DESC LIMIT 4;

-- JOIN

SELECT city.Name, city.Population, countrycode, country.name
  FROM city LEFT JOIN country ON city.countrycode = country.code LIMIT 2;

-- Exclusive left join

SELECT city.Name, city.Population, countrycode, country.name
  FROM city LEFT JOIN country ON city.countrycode = country.code
  WHERE countrycode IS NULL;
