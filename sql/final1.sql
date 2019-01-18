ALTER FUNCTION func (@cstID nvarchar(100))
RETURNS @table__ TABLE (prCnt int, gnacApranqneriTiv int)--, minQanakApranq nvarchar(10))
AS
BEGIN

DECLARE @prCnt int, @gnacApranqGumar int, @minQanakApranq nvarchar(100)
SELECT @prCnt = SUM(DISTINCT(Products.ProductID))
FROM Orders 
    JOIN [Order Details] on [Order Details].OrderID=Orders.OrderID 
    JOIN Products on [Order Details].ProductID=Products.ProductID
    WHERE Orders.CustomerID = 'ANTON' 
    GROUP BY Orders.OrderID, Products.ProductID
SELECT @gnacApranqGumar = SUM([Order Details].Quantity * [Order Details].UnitPrice * (1 - [Order Details].Discount))  
FROM Orders 
    JOIN [Order Details] on [Order Details].OrderID=Orders.OrderID 
    --JOIN Products on [Order Details].ProductID=Products.ProductID
    WHERE Orders.CustomerID = 'ANTON' 
    --GROUP BY Orders.OrderID, Products.ProductID

SELECT @prCnt, @gnacApranqGumar

INSERT INTO @table__ VALUES(@prCnt, @gnacApranqGumar)
return
END
go
select * from dbo.func('ANTON')




select * from Customers
