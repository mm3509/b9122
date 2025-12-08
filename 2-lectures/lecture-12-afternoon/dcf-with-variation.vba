' New line: take an argument
Public Function DCF(variation As Double) As Double

Dim CashFlow As Double
Dim DiscountRate As Double
Dim Row As Integer
Dim Year As Integer
Dim Periods As Integer
Dim Denominator As Double

' New line: a new variable
Dim Perturbation As Double

DiscountRate = Cells(1, 4).Value
NetPresentValue = 0

For Row = 4 To 21
    Year = Cells(Row, 1).Value
    CashFlow = Cells(Row, 2).Value
    Periods = (Year - 2025)
    ' New line: define the variation as a factor
    Variation_factor = 1 + variation * (Rnd() * 2 - 1)
    Denominator = (1 + DiscountRate) ^ Periods
    DCF = DCF + CashFlow * Variation_factor / Denominator
Next Row

End Function
