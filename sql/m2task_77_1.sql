--Կազմել պրոցեդուրա, որն ըստ Employee – ների, կստանա պատ-
--վերների ընդհանուր գինը և ամենամեծ գումարով պատվերի օրը (ֆունկցիայի միջոցով):

ALTER FUNCTION biggestValueDate (@emplID int)
RETURNS DATETIME
BEGIN
	RETURN (SELECT table_.date_  FROM (SELECT TOP 1 WITH TIES   
		SUM([Order Details].Unitprice * [Order Details].Quantity *
			(1-[Order Details].Discount)) as gumar, Orders.OrderDate as date_
		FROM [Order Details] 
			JOIN  Orders ON [Order Details].OrderID = Orders.OrderID
		WHERE Orders.EmployeeID=@emplID
		GROUP BY Orders.OrderID, Orders.OrderDate
		ORDER BY (gumar) DESC) as table_)
END

ALTER PROC proc_ 
AS
	SELECT  
		Orders.EmployeeID, 
		SUM([Order Details].Unitprice * [Order Details].Quantity * (1-[Order Details].Discount)),
		dbo.biggestValueDate(Orders.EmployeeID)
	FROM  [Order Details]
		JOIN  Orders ON [Order Details].OrderID = Orders.OrderID
	GROUP BY Orders.EmployeeID
GO

EXECUTE proc_
GO

