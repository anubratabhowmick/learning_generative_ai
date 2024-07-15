TEMPLATE1 = """
    Text: {text}
    You are an expect MCQ maker. Given the above text, it is your job to \
    create quiz of {number} multiple choice questions for {subject} students in {tone} tone.
    Make sure the questions are not repeated and check all the questions to be conforming the text as well.
    Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
    ### RESPONSE_JSON
    {response_json}
"""

TEMPLATE2 = """ 
    You are an expert in English Grammar and a superstar in writing. Given a Multiple Choice Quiz for {subject} students, \
    you need to evaluate the complexity of the questions and give a complete analysis of the quiz. Only use at max 50 words for complexity and \
    if the quiz is not as per the cognitive and analytical abilities of the students, \
    update the quiz questions which needs to be changed and change the tone such that it perfectly fits the abilities of the students.
    Quiz MCQs:
    {quiz}
    
    Check the above quiz from an expert English writer.
"""
