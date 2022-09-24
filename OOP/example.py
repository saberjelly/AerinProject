from operators import addition, subtraction, multiplication, division
from operators import UtilityTool, UtilityBelt, DataSet

a = 10
b = 2

print(addition(a,b), subtraction(a,b), multiplication(a,b), division(a,b))
operator_obj = UtilityTool(a,b)
print(operator_obj.addition(), operator_obj.subtraction(), operator_obj.multiplication(), operator_obj.division())

child_object = UtilityBelt(a, b)
print(child_object.addition(), child_object.subtraction(), child_object.multiplication(), child_object.division())
print(child_object.power())

ListOfNumbers = [10,11,12,13,14,15,16,17,18,19]

DS = DataSet(ListOfNumbers)
print(DS[0])
print(DS.__getitem__(0))
print(DS(9))
print(DS.__call__(8))
