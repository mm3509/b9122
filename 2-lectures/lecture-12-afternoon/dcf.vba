Public Function DCF() As Double

Dim CashFlow As Double
Dim DiscountRate As Double
Dim Row as Integer
Dim Year As Integer
Dim Periods As Integer
Dim Denominator as Double

DiscountRate = Cells(4, 1).Value
NetPresentValue = 0

For Row = 4 To 21
    Year = Cells(Row, 1).Value
    CashFlow = Cells(Row, 2).Value
    Periods = (Year - 2025)
    Denominator = (1 + DiscountRate) ^ Periods
    DCF = DCF + CashFlow / Denominator
Next Row

End Sub
