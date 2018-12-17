--Պատվերների միջին արժեքից բարձր գումարային արժեքով պատվերներ ունեցող
--Employee-ների համար կստանա պատվերների ընդհանուր գինը և
--ամենափոքր գումարով պատվերի գումարային արժեքը և պատվերների ցուցակը:
DEALLOCATE curs
USE NORTHWND
DECLARE curs CURSOR
FOR

    SELECT Orders.EmployeeID, COUNT(Orders.OrderID)
    FROM Orders
    GROUP BY Orders.EmployeeID

    HAVING COUNT(Orders.OrderID) >(Select AVG(emp.qanak) FROM  
        (SELECT Orders.EmployeeID, COUNT(Orders.OrderID) as qanak
            FROM Orders

            GROUP BY Orders.EmployeeID) as emp) 

OPEN curs
DECLARE @qanak int, @empl int
FETCH FROM curs INTO 
@empl, @qanak
SELECT @empl, @qanak
WHILE @@FETCH_STATUS = 0
    BEGIN
        SELECT 
        SUM(([Order Details].Quantity * [Order Details].UnitPrice)
            * (1-[Order Details].Discount))
        FROM Orders
        JOIN [Order Details] on [Order Details].OrderID=Orders.OrderID
        WHERE Orders.EmployeeID = @empl 
        GROUP BY orders.EmployeeID

        SELECT TOP 1 WITH TIES SUM(([Order Details].Quantity * [Order Details].UnitPrice)
            * (1-[Order Details].Discount)) as gumar, Orders.OrderDate 
        FROM Orders 
        JOIN [Order Details] on [Order Details].OrderID=Orders.OrderID
        WHERE Orders.EmployeeID = @empl
        GROUP BY Orders.OrderID, Orders.OrderDate
        ORDER BY (gumar) DESC

        FETCH FROM curs INTO
        @empl, @qanak
        SELECT @empl, @qanak
    END 
CLOSE curs

--------------------------------------------------------
-- ազյուսակ տպիպ փոփում ստանալ յուր․ օրվա վաճառված ապրանքների ընդհանուր գումաորը
DECLARE curs_ CURSOR FOR
SELECT orderid_ = (Orders.OrderDate), gumar_ = SUM([Order Details].Quantity * [Order Details].UnitPrice
    * (1-[Order Details].Discount))
FROM Orders				
JOIN [Order Details] on [Order Details].OrderID=Orders.OrderID
-- WHERE Orders.EmployeeID = @empl
GROUP BY (Orders.OrderDate)
--ORDER BY (Orders.OrderDate) DESC

DECLARE @table_ TABLE ( order_date DATETIME, 
    gumar int)
DECLARE @order_date_ DATETIME, @gumar_ int 
OPEN curs_
FETCH FROM curs_ INTO @order_date_, @gumar_
WHILE @@FETCH_STATUS=0
    BEGIN 
        INSERT INTO @table_ 
        VALUES(
            @order_date_,
            @gumar_
        )
        FETCH FROM curs_ into @order_date_, @gumar_
END
SELECT * from @table_
DEALLOCATE curs_
