from cgitb import text
from multiprocessing.connection import answer_challenge
from types import new_class
from data import question_data
from question_model import Question

question_bank = []

for question in question_data:
    question_text = question['text']
    answer_text = question['answer']
    new_question = Question(answer_text, question_text)
    question_bank.append(new_question)




    
      
