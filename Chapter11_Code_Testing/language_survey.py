"""Testing Code"""

from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查AnonymousSurvey的对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 现实问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response =='q':
        break
    my_survey.store_reponse(response)

# 显示调查结果
print("\nThank you to everyone who participanted in the survey!")
my_survey.show_results()