
class A:
    def method_A(self):
        return "Method A"

class B(A):
    def method_B(self):
        return "Method B"

class C:
    def method_C(self):
        return "Method C"

class D(B, C):
    def method_D(self):
        return "Method D"

obj = D()
print(obj.method_A())  # Output: Method A
print(obj.method_B())  # Output: Method B
print(obj.method_C())  # Output: Method C
print(obj.method_D())  # Output: Method D
