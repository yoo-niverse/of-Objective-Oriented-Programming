''' 신 객체인 Student 클래스를 단일 책임 원칙을 적용하여 분리하기 '''
class Student:
    ''' 학생의 정보, 정보변경, 성적표 등 신상과 관련된 기능을 수행하는 클래스 '''
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major
        self.grade = Grade()
            ''' grade 인스턴스는 Grade 클래스의 객체로 지정해주어야 해당 클래스의 메소드를 실행할 수 있다. '''

    def change_student_info(self, new_name, new_id, new_major):
        self.name = new_name
        self.id = new_id
        self.major = new_major

    def print_report_card(self):
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}"\
        .format(self.name, self.id, self.major, self.grade.get_average_gpa()))

class Grade:
    ''' 학생의 성적, 평점계산 등의 기능을 수행하는 클래스 '''
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        return sum(self.grades) / len(self.grades)

# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

# 학생 성적 추가

younghoon.grade.add_grade(3.0)
younghoon.grade.add_grade(3.33)
younghoon.grade.add_grade(3.67)
younghoon.grade.add_grade(4.3)
 ''' grade 인스턴스는 Grade 클래스의 객체로 지정되었으므로 add_grade 메소드 호출이 가능하다. '''

# 학생 성적표
younghoon.print_report_card()


'''
[기능 분리 전 God Object]
class Student:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major
        self.grades = []

    def change_student_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산 메소드"""
        return sum(self.grades) / len(self.grades)

    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}"\
        .format(self.name, self.id, self.major, self.get_average_gpa()))'''
