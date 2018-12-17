--պատվերների միջին քանակից փոքր քանակով պատտվերներ ունեցող
֊֊customer֊ների համար կստանա պատվերների ընդհանուր գինը
--, ամենաթանկ ապրանքի առարիչի անունը (shippers) CompanyName
--և պատվերների ցուցակ
DECLARE curs CURSOR 
FOR
    SELECT
    Orders.CustomerID, COUNT(Orders.OrderID) 
    FROM Orders
    GROUP BY Orders.CustomerID
    HAVING COUNT(Orders.CustomerID) < (SELECT AVG(customer_.quantity) FROM
        (SELECT Orders.CustomerID, COUNT(Orders.OrderID) as quantity 
            FROM Orders
GROUP BY Orders.CustomerID) as customer_)

OPEN curs
DECLARE @customer_id nvarchar(20), @quantity int
FETCH FROM curs INTO @customer_id , @quantity

WHILE @@FETCH_STATUS = 0
    BEGIN
        SELECT SUM([Order Details].Quantity * [Order Details].UnitPrice * (1 - [Order Details].Discount))
        FROM [Order Details] JOIN Orders ON  [Order Details].OrderID = Orders.OrderID
        WHERE Orders.CustomerID = @customer_id
        FETCH FROM curs INTO @customer_id , @quantity

        SELECT TOP 1 WITH TIES SUM([Order Details].Quantity * [Order Details].UnitPrice 
            * (1 - [Order Details].Discount)) as orderPrice, Shippers.CompanyName
        FROM [Order Details] JOIN Orders ON  [Order Details].OrderID = Orders.OrderID
        JOIN Shippers ON Shippers.ShipperID = Orders.ShipVia
        WHERE Orders.CustomerID = @customer_id
        GROUP BY Shippers.CompanyName
        ORDER BY orderPrice DESC

        FETCH FROM curs INTO @customer_id , @quantity
    END
DEALLOCATE curs
----------------------------------------------
DECLARE curs_ CURSOR
FOR 
    SELECT Employees.EmployeeID, COUNT(Orders.OrderID)
    FROM Employees JOIN Orders ON Orders.EmployeeID = Employees.EmployeeID
    GROUP BY Employees.EmployeeID

DECLARE @empID int, @quantity int
DECLARE @table_ TABLE (mpID int , quantity int)
OPEN curs_
FETCH FROM curs_ INTO @empID, @quantity
WHILE @@FETCH_STATUS = 0
    BEGIN
        INSERT INTO @table_
        VALUES (@empID, @quantity)
        FETCH FROM curs_ INTO @empID, @quantity
    END
SELECT * FROM @table_
DEALLOCATE curs_

--------------------------------------------
-- ամենափոքր թվով վաճառվածները
SELECT
Orders.CustomerID, COUNT(Orders.OrderID)
FROM Orders
GROUP BY Orders.CustomerID
HAVING COUNT(Orders.CustomerID) < (SELECT TOP 1 WITH TIES (customer_.quantity) FROM
	(SELECT Orders.CustomerID, COUNT(Orders.OrderID) as quantity
	FROM Orders
	GROUP BY Orders.CustomerID) as customer_
	ORDER BY quantity)
