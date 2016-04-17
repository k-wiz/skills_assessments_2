class Student(object):
    
    def __init__(self, first_name, last_name, address):
        
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):

    def __init__(self, question, correct_answer):

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):



        #print self.question
        #print self.correct_answer
        user_answer = raw_input(">> ")
        #print user_answer
        if user_answer == self.correct_answer:
            return True
        else:
            return False




class Exam(object):

    def __init__(self, name):

        self.name = name
        self.questions = []



    def add_question(self, question, correct_answer):

        self.questions.append(question)





kelli = Student("kelli", "wisuri", "8 Admiral Dr.")

midterm = Exam("midterm")



