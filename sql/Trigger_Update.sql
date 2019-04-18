CREATE TRIGGER updateInfoOnUpdate ON [Order Details]
FOR UPDATE AS
BEGIN

IF ((SELECT ProductID FROM inserted) = (SELECT ProductID FROM deleted))
    UPDATE nor SET Qnt = Qnt + ((SELECT Quantity FROM inserted) - (SELECT Quantity FROM deleted)
	  WHERE (SELECT ProductID FROM inserted) = nor.PrID AND
    nor.Dat = (SELECT OrderDate FROM Orders WHERE Orders.OrderID =
	 (SELECT OrderID FROM inserted))
ELSE
    BEGIN
        UPDATE nor SET Qnt = Qnt - (SELECT Quantity FROM deleted)

        IF EXISTS(
            SELECT Dat FROM nor WHERE (SELECT ProductID FROM inserted) =
			 nor.PrID AND
            nor.Dat = (SELECT OrderDate FROM Orders WHERE Orders.OrderID =
			 (SELECT OrderID FROM inserted))
        )
            UPDATE nor SET Qnt = Qnt + (SELECT Quantity FROM inserted)
			 WHERE (SELECT ProductID FROM inserted) = nor.PrID AND
            nor.Dat = (SELECT OrderDate FROM Orders WHERE Orders.OrderID =
			 (SELECT OrderID FROM inserted))
        ELSE
            INSERT nor VALUES((SELECT ProductID FROM inserted),
			 (SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM inserted)),
			  (SELECT Quantity FROM inserted))
    END
END
