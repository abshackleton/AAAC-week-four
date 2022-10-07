

SELECT username
FROM users



SELECT username
FROM users
WHERE username = 'adams'


SELECT username, ordered_product
FROM users INNER JOIN orders ON users.username = orders.username
WHERE users.username = 'adams'


INSERT INTO users (username, first_name, second_name, address)
VALUES ('markt', 'Mark', 'Twain', '99 Finn Avenue')

INSERT INTO users (username, first_name, second_name, address)
SELECT username, name, surname, residence
FROM people


UPDATE users
SET address = '101 Finn Avenue'
WHERE username = 'markt'

DELETE FROM users
WHERE username = adams


SELECT username, COUNT(ordered_product) count_of_products
FROM users INNER JOIN orders ON users.username = orders.username
WHERE users.username = 'adams'
GROUP BY username


CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);

ALTER TABLE users
ADD COLUMN star_sign TEXT