class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    # Equality test method
    def __eq__(self, other):
        # Compare based on the student's name
        return self.name == other.name
    
    # Less than: <
    def __lt__(self, other):
        return self.name < other.name
    
    # Greater than or equal to: >=
    def __ge__(self, other):
        return self.name >= other.name
    


def main():
    s1 = Student("Alice", 1001)
    s2 = Student("Bob", 1002)
    s3 = Student("Alice", 1003)

    print(s1 == s2)   # Expected: False
    print(s1 == s3)   # Expected: True

    print(s1 < s2)    # True ("Alice" < "Bob")
    print(s2 < s1)    # False ("Bob" < "Alice")

    # Greater than or equal tests
    print(f"{s1 >= s2}: {s1 >= s2}")  # False: False
    print(f"{s2 >= s1}: {s2 >= s1}")  # True: True
    print(f"{s1 >= s3}: {s1 >= s3}")  # True: True


if __name__ == "__main__":
    main()
