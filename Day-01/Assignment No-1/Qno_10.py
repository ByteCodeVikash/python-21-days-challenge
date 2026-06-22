"""
Qno-10.
Accept two integer inputs into two variables, ‘A‘ and ‘B‘. Swap the values of these two variables
without using a third temporary variable, and print their new values.

"""

A=int(input("Enter A : "))
B=int(input("Enter B : "))

A,B=B,A
print("A=",A)
print("B=",B)