SELECT DISTINCT rating FROM books;
SELECT title, price_inr FROM books WHERE rating=5 ORDER BY price_inr DESC LIMIT 10;
SELECT COUNT(*) FROM books WHERE in_stock=1;
SELECT title FROM books WHERE price_inr BETWEEN 500 AND 1000;
SELECT b.title, c.name FROM books b JOIN categories c ON b.category_id=c.id;
