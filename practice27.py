# 다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
# 이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.

from dataclasses import dataclass

@dataclass
class Student:
    kor : str
    eng : str
    math : str


    def sum_score(self):

        sum = self.kor + self.eng + self.math

        return sum
        

    
a = Student(100, 100, 100)

print(a.sum_score())
