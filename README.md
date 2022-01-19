# Data-Science-Intern-Challenge

Summer 2022 Data Science Intern Challenge

Question 1: Given some sample data, write a program to answer the following: click here to access the required data set

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

1. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.

	The calculation of AOV might get wrong because the total amount of orders might be calculated with the COUNT() function, so the total amount of orders will be the number of rows. I think when I  need to get total amount of orders, I would use SUM() function on total_items, then I’ll get the correct answer for AOV

2. What metric would you report for this dataset?
# a. I need to figure out the SUM of total order amount
sum_oa = df['order_amount'].sum()
# b. I need to figure out the SUM of total order items
sum_ti = df['total_items'].sum()
print(sum_oa)
print(sum_ti)

# now we know the sum of total order amount is 15725640
# and the total order items is 43936
# then we can calculate the AVO by dividing sum_oa by sum_ti
AOV = sum_oa / sum_ti
AOV = "%.2f" % AOV
print(AOV)
AOV =  $ 357.92
	
1. What is its value?
	AOV  is $357.92


Question 2: For this question you’ll need to use SQL. Follow this link to access the data set required for the challenge. Please use queries to answer the following questions. Paste your queries along with your final numerical answers below.

1. How many orders were shipped by Speedy Express in total?

SELECT
	COUNT(o.OrderID) AS TotalOrders
FROM
	Orders AS o
LEFT JOIN
	Shippers AS s
    ON
    o.ShipperID = s.ShipperID
WHERE
	s.ShipperName = 'Speedy Express'

ANSWER: 54

2. What is the last name of the employee with the most orders?

SELECT
	e.LastName
FROM
	Employees AS e
LEFT JOIN
	Orders AS o
    ON
    e.EmployeeID = o.EmployeeID
GROUP BY
	LastName
ORDER BY
	COUNT(OrderID) DESC
LIMIT 1;

ANSWER: Peacock

3. What product was ordered the most by customers in Germany?

WITH Products_Ordered AS
(SELECT o.OrderID, c.Country, od.Quantity, p.ProductName
FROM Orders AS o, OrderDetails AS od
JOIN Customers AS c ON o.CustomerID = c.CustomerID
JOIN Products ON od.ProductID = p.ProductID
WHERE Country='Germany’)

WITH Product_Orders AS
)SELECT ProductName, Quantity, COUNT(*) as 'Orders'
FROM Products_Ordered
GROUP BY ProductName)

SELECT ProductName, Quantity, Orders, (Quantity * Orders) AS TotalOrdered
FROM Product_Orders
ORDER BY TotalOrdered desc
LIMIT 1;
