class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        total = 0
        for m in self.marks:
            total += m
        return total / len(self.marks)
    
s1 = Student("Alice", [85, 90, 78, 92, 88])

print(s1.average())
