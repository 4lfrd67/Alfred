class Student:
    def __init__(self, student_id, name, course, year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level

    def display(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Course: {self.course} | Year: {self.year_level}")


class DynamicArray:
    def __init__(self):
        self.capacity = 5
        self.size = 0
        self.arr = [None] * self.capacity

    def add(self, student):
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = student
        self.size += 1
        print("Student added successfully.")

    def resize(self):
        print("Array is full. Increasing array capacity...")
        self.capacity *= 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        print(f"New Capacity: {self.capacity}")

    def display_students(self):
        if self.size == 0:
            print("No student records found.")
            return

        for i in range(self.size):
            self.arr[i].display()

    def search_student(self, student_id):
        for i in range(self.size):
            if self.arr[i].student_id == student_id:
                print("Student Found:")
                self.arr[i].display()
                return

        print("Student ID not found.")

    def update_student(self, student_id, new_name, new_course, new_year):
        for i in range(self.size):
            if self.arr[i].student_id == student_id:
                self.arr[i].name = new_name
                self.arr[i].course = new_course
                self.arr[i].year_level = new_year
                print("Student information updated.")
                return

        print("Student ID not found.")

    def remove_student(self, student_id):
        index_to_remove = -1

        for i in range(self.size):
            if self.arr[i].student_id == student_id:
                index_to_remove = i
                break

        if index_to_remove == -1:
            print("Student ID not found.")
            return

        for i in range(index_to_remove, self.size - 1):
            self.arr[i] = self.arr[i + 1]

        self.arr[self.size - 1] = None
        self.size -= 1
        print("Student removed successfully.")

    def display_array_information(self):
        print(f"Current Number of Students: {self.size}")
        print(f"Current Array Capacity: {self.capacity}")


def main_part1():
    da = DynamicArray()

    while True:
        print("\n--- STUDENT RECORD MANAGER ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Remove Student")
        print("6. Display Array Information")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            s_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            course = input("Enter Course: ")

            try:
                year = int(input("Enter Year Level: "))
                da.add(Student(s_id, name, course, year))
            except ValueError:
                print("Invalid Year Level. Please try again.")

        elif choice == 2:
            da.display_students()

        elif choice == 3:
            s_id = input("Enter Student ID to search: ")
            da.search_student(s_id)

        elif choice == 4:
            s_id = input("Enter Student ID to update: ")
            name = input("Enter New Name: ")
            course = input("Enter New Course: ")

            try:
                year = int(input("Enter New Year Level: "))
                da.update_student(s_id, name, course, year)
            except ValueError:
                print("Invalid Year Level.")

        elif choice == 5:
            s_id = input("Enter Student ID to remove: ")
            da.remove_student(s_id)

        elif choice == 6:
            da.display_array_information()

        elif choice == 7:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_part1()
