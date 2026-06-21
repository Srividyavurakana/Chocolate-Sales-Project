-- Total Sales
SELECT SUM(Amount) FROM chocolates;

-- Best Selling Products
SELECT Product, SUM(Amount)
FROM chocolates
GROUP BY Product
ORDER BY SUM(Amount) DESC;

-- Monthly Revenue
SELECT Month, SUM(Amount)
FROM chocolates
GROUP BY Month;