Sub Button2_Click()
'
' Documentation, like a doc-string
'

    'Comments start with single quote.

    ' Assign to a range.
    Range("A1:A10").value = "Visual Basic"
    
    ' Perform calculations.
    Range("C11").value = Range("A11").value + Range("B11").value
    
    ' Static typing: you have to declare a type.
    Dim val As String
    val = "Hello world"
    Range("A12").value = val
    
    ' Asking for user input.
    Dim YourName As String
    YourName = InputBox("Enter your name")
    Range("A13").value = YourName
    
    ' The target cells can be dynamic, specified in code.
    Dim row As String
    Dim col As String
    row = "A"
    col = "14"
    
    ' Concatenate strings with +, like Python.
    Range(row + col) = "Dynamic filling"
    
End Sub


Function CubeRoot(num As Double) As Double
CubeRoot = num ^ (1 / 3)
End Function
