class Student:
    def __init__(self, name, age, is_single):
        self.name = name  
        self.age = age  
        self.is_single = is_single  
        self.grades = []  
    def add_grade(self, grade):
        self.grades.append(grade)
    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
    def __str__(self):
        return f"姓名：{self.name}，平均成绩：{self.average_grade():.2f}"  
    def print_status(self):
        status = "单身" if self.is_single else "非单身"
        print(f"姓名：{self.name}，年龄：{self.age}，单身否：{status}")
if __name__ == "__main__":
    student1=Student("张三",18,True)
    student1.add_grade(85.0)
    student1.add_grade(90.5)
    student1.add_grade(78.5)
    print(student1) 
    student1.print_status()  