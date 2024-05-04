class A:
    def method_A(self):
        return "Method A"

class B:
    def method_B(self):
        return "Method B"

class C(A, B):
    def method_C(self):
        return "Method C"

obj = C()
print(obj.method_A())  # Output: Method A
print(obj.method_B())  # Output: Method B
print(obj.method_C())  # Output: Method C
