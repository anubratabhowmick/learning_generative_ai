import json
import PyPDF2
import traceback

def read_file(file_name):
    if file_name.name.endswith('.pdf'):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file_name)
            text = ""
            
            for page in pdf_reader.pages:
                text += page.extract_text()
                
            return text
        
        except Exception as e:
            raise Exception("Error reading the PDF file.")
        
    elif file_name.name.endswith('.txt'):
        return file_name.read().decode('utf-8')
    
    else:
        raise Exception(
            "Unsupported file format. Only PDF/text files are supported."
        )
        
        
def get_table_data(quiz_str):
    try:
        # Convert the quiz from string to JSON
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []
        
        # Iterate over the quiz dictionary and extract the required information
        for key, value in quiz_dict.items():
            mcq = value['mcq']
            
            options = ' || '.join(
                [f'{option}->{option_value}' for option, option_value in value["options"].items()]
            )
            
            correct = value['correct']
            
            quiz_table_data.append({
                'MCQ': mcq,
                'Choices': options,
                'Correct Answer': correct
            })
            
        return quiz_table_data
    
    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False