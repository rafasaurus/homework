CREATE TRIGGER updateInsert ON [Order Details]
FOR INSERT AS 
IF EXISTS(
    SELECT Dat FROM nor WHERE (SELECT ProductID FROM inserted) = nor.PrID AND
    nor.Dat = (SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM inserted))
)
    UPDATE nor SET Qnt = Qnt + (SELECT Quantity FROM inserted) WHERE (SELECT ProductID FROM inserted) =
	 nor.PrID AND
    nor.Dat = (SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM
	 inserted))
ELSE
    INSERT nor VALUES((SELECT ProductID FROM inserted), (SELECT OrderDate FROM Orders WHERE Orders.OrderID = 
	(SELECT OrderID FROM inserted)), SELECT Quantity FROM inserted)




