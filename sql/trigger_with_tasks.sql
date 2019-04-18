Խնդրի դրվածքը.
Ստեղծել նոր աղյուսակ, որտեղ կլինեն հետևյալ դաշտերը․
1․ProductID ապրանքատեսակի համարը
2. Quantity քանակը
3․ OrderDate պատվերի օրը
Աղյուսակում գրանցվելու է պատվերի մասին հավելյալ ինֆորմացիա՝ թե որ օրը որ ապրանքատեսակից ինչքան է պատվիրվել։
Ամեն անգամ Order Details աղյուսակում պատվեր ավելացնելու, փոփոխելու կամ ջնջելու դեպքում տրիգերի միջոցով ստեղծված աղյուսակը պահել թարմացված։

Insert Trigger
Տրիգերը աշխատում է, երբ նոր տող է ավելացվում Order Details աղյուսակում։ Երբ այդ օրը պատվիրվում է արդեն իսկ պատվիրված ապրանքատեսակ, ապա նոր ստեղծված աղյուսակում փոփոխվում է միայն քանակը, հակառակ դեպքում ավելանում է նոր տող։
CREATE TRIGGER updateInfoOnInsert ON [Order Details]
FOR INSERT AS 
IF EXISTS(
    SELECT OrderDate FROM OrderDetailInfo WHERE (SELECT ProductID FROM inserted) = OrderDetailInfo.ProductID AND
    OrderDetailInfo.OrderDate = (SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM inserted))
)
    UPDATE OrderDetailInfo SET Quantity = Quantity + (SELECT Quantity FROM inserted) WHERE (SELECT ProductID FROM inserted) = OrderDetailInfo.ProductID AND
    OrderDetailInfo.OrderDate = (SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM inserted))
ELSE
    INSERT OrderDetailInfo VALUES((SELECT ProductID FROM inserted), (SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM inserted)), SELECT Quantity FROM inserted)
Delete Trigger
Տրիգերը աշխատում է, երբ Order Details աղյուսակում տող է ջնջվում։ Երբ այդ օրը չկա այլևս ուրիշ գրառում, ապա նոր ստեղծված աղյուսակից ջնջվում է համապատասխան տողը, հակառակ դեպքում նվազում է քանակը։

CREATE TRIGGER updateInfoOnDelete ON [Order Details]
FOR DELETE AS
IF (
    (SELECT Quantity FROM OrderDetailInfo WHERE OrderDetailInfo.OrderDate = ((SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM deleted)) AND
    (SELECT ProductID FROM deleted) = OrderDetailInfo.ProductID) = (SELECT Quantity FROM deleted)
)
    DELETE OrderDetailInfo WHERE OrderDetailInfo.OrderDate = (SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM deleted)) AND
    (SELECT ProductID FROM deleted) = OrderDetailInfo.ProductID
ELSE
    UPDATE OrderDetailInfo SET Quantity = Quantity - (SELECT Quantity FROM deleted) WHERE OrderDetailInfo.OrderDate = (SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM deleted)) AND
    (SELECT ProductID FROM deleted) = OrderDetailInfo.ProductID


CREATE TABLE OrderDetailInfo(
    ProductID int, 
    OrderDate datetime,
    Quantity int,
)

Update Trigger
Տրիգերը աշխատում է, երբ Order Details աղյուսակում տող է փոփոխվում։ կախված փոփոխված տվյալների, նորաստեղծ աղյուսակում կատարվում են համապատասխան փոփոխություններ։ Հաշվի առնված են այն դեպքերը, երբ փոփոխվում է ապրանքատեսակը, քանակը կամ պատվերի օրը։ 
CREATE TRIGGER updateInfoOnUpdate ON [Order Details]
FOR UPDATE AS
BEGIN
IF ((SELECT ProductID FROM inserted) = (SELECT ProductID FROM deleted)) -- եթե փոփոխվել է 
    -- տրամաբանորեն պատվերի քանակը պետք է փոփոխվի, դրանից էլ կախված մյուս կոմպոնենտները
    UPDATE OrderDetailInfo SET Quantity = Quantity + ((SELECT Quantity FROM inserted) - (SELECT Quantity FROM deleted) 
        WHERE 
            (SELECT ProductID FROM inserted) = OrderDetailInfo.ProductID 
                AND
            OrderDetailInfo.OrderDate = (SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM inserted)))
ELSE -- եթե ավելացվել(inserted) է կամ, կամ ջնջվել է(deleted)
    BEGIN 
        -- եթե ջնջվել է
        UPDATE OrderDetailInfo SET Quantity = Quantity - (SELECT Quantity FROM deleted)
        -- եթե չի ջնջվել ապա փոփոխություն տեղի չի ունցել, այսինքն կարող ենք նույն սկոպում շարունակել
        IF EXISTS(
                -- եթե ավելացվել է և ProductID-ն և OrderDate-ը (եթե ավելացվել է աղյուսակում գրառում ապա)
                -- եթե օրը inserted է եղել, այսինքն տեղի է ունեցել inserted ապա
                SELECT OrderDate FROM OrderDetailInfo 
                    WHERE (SELECT ProductID FROM inserted) = OrderDetailInfo.ProductID 
                        AND
                    OrderDetailInfo.OrderDate = (SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM inserted))
            ) -- END_OF_EXISTS

            UPDATE OrderDetailInfo SET Quantity = Quantity + (SELECT Quantity FROM inserted)
                WHERE 
                    (SELECT ProductID FROM inserted) = OrderDetailInfo.ProductID 
                        AND
                    OrderDetailInfo.OrderDate = (SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM inserted))
        ELSE
            INSERT OrderDetailInfo VALUES((SELECT ProductID FROM inserted), (SELECT OrderDate FROM Orders WHERE Orders.OrderID = (SELECT OrderID FROM inserted)), (SELECT Quantity FROM inserted))
    END
END
