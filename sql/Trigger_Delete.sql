CREATE TRIGGER updateDelete ON [Order Details]
FOR DELETE AS
IF (
    (SELECT Qnt FROM nor WHERE nor.Dat =
	 ((SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM deleted)) AND
    (SELECT ProductID FROM deleted) = OrderDetailInfo.ProductID) = (SELECT Quantity FROM deleted)
)
    DELETE nor WHERE nor.Dat = (SELECT OrderDate FROM Orders WHERE
	 Orders.OrderID = (SELECT OrderID FROM deleted)) AND
    (SELECT ProductID FROM deleted) = nor.PrID
ELSE
    UPDATE nor SET Qnt = Qnt - (SELECT Quantity FROM deleted) WHERE
	 nor.Dat = (SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM deleted)) AND
    (SELECT ProductID FROM deleted) = nor.PrID