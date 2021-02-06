class QuizBrain:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def next_quesetion(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1

        answer = input(f"\nQ{self.question_number}: {current_question.question}(TRUE/FALSE)? ")
        self.check_answer(answer,current_question.answer)

    def still_has_questions(self):
        return len(self.question_list) > self.question_number


    def check_answer(self,u_answer , answer):

        if u_answer.lower() == answer.lower() :
            self.score+=1
            print("you got it right!")
        else:
            print("That's wrong")
        print(f"your score: {self.score}/{self.question_number}")


    def finish(self):
        if len(self.question_list) == self.question_number:
            print("****You've completed the quiz****")
            print(f"Your final score is: {self.score}/{self.question_number}")

