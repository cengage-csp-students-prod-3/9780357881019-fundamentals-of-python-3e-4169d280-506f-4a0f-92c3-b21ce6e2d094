# Write your code here
class Student:
    def __init__(self, name):
        self.name = name

    # Equality: ==
    def __eq__(self, other):
        return self.name == other.name

    # Less than: <
    def __lt__(self, other):
        return self.name < other.name

    # Greater than or equal to: >=
    def __ge__(self, other):
        return self.name >= other.name


def main():
    # Create Student objects
    s1 = Student("Alice")
    s2 = Student("Bob")
    s3 = Student("Alice")

    # Test equality
    print(f"{s1 == s2}: {s1 == s2}")   # False: False
    print(f"{s1 == s3}: {s1 == s3}")   # True: True

    # Test less than
    print(f"{s1 < s2}: {s1 < s2}")     # True: True
    print(f"{s2 < s1}: {s2 < s1}")     # False: False

    # Test greater than or equal
    print(f"{s1 >= s2}: {s1 >= s2}")   # True: True or False depending on names
    print(f"{s2 >= s1}: {s2 >= s1}")   # True: True
    print(f"{s1 >= s3}: {s1 >= s3}")   # True: True

    # Additional tests (to reach 10 lines total)
    print(f"{s2 >= s3}: {s2 >= s3}")   # True: True
    print(f"{s2 == s2}: {s2 == s2}")   # True: True
    print(f"{s3 < s2}: {s3 < s2}")     # True: True


if __name__ == "__main__":
    main()