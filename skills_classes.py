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
        """Asks question and evaluates whether user-provided answer
        is correct. """

        print self.question
        user_answer = raw_input(">> ")
        if user_answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):

    def __init__(self, name):

        self.name = name
        self.questions = []



    def add_question(self, question, correct_answer):
        """Note: I don't feel good about the way add_question and the Question
        class relate (or fail to relate) to each other, but I wasn't sure how
        to fix it. 
        """

        new_question = Question(question, correct_answer)
        self.questions.append(new_question)



    def administer(self):
        """ Administers exam, returns user's score."""
        
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1
        return score



def take_test(exam, student):
    """Administers the exam, assigns the score to the student instance
    in a new attribute called score. """


    score = exam.administer()
    student.score = score


def example():

    """Creates an exam; adds questions to exam; creates a student; 
    administers test to student; prints student's score. """

    midterm = Exam("midterm")
    midterm.add_question("Who wrote python?", "Guido van Rossum")
    midterm.add_question("What's the best color?", "green")
    kelli = Student("kelli", "wisuri", "8 Admiral Dr.")

    print "%s's score is %s." % (kelli.first_name, kelli.score)






# kelli = Student("kelli", "wisuri", "8 Admiral Dr.")

# midterm = Exam("midterm")

# question1 = Question("Who wrote python?", "Guido van Rossum")

# question2 = Question("What's the best color?", "green")







