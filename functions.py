import json
import os
import PyPDF2  # Make sure PyPDF2 is installed and imported
from PyPDF2 import PdfReader


def read_pdf(file_path):
  text = ''
  with open(file_path, 'rb') as file:
    pdf_reader = PdfReader(file)
    for page in pdf_reader.pages:
      text += page.extract_text()
  return text


def create_assistant(client):
  assistant_file_path = 'assistant.json'

  if os.path.exists(assistant_file_path):
    with open(assistant_file_path, 'r') as file:
      assistant_data = json.load(file)
      assistant_id = assistant_data['assistant_id']
      print("Loaded existing assistant ID.")
  else:


    # pdf_text = read_pdf('Undergraduate.pdf')
    pdf_files = ['ADS500B_Content.pdf', 'ADS500B_Book.pdf']

    all_pdf_text = ""

    for pdf_file in pdf_files:
      pdf_text = read_pdf(pdf_file)
      all_pdf_text = all_pdf_text + pdf_text

    # Use the text from the PDF to create the file for the assistant
    file = client.files.create(file=all_pdf_text.encode('utf-8'),
                               purpose='assistants')

    assistant = client.beta.assistants.create(name="AI TA Assistant",
                                              instructions="""
        You are an expert Teaching Assistant for ADS500B, specializing in guiding students through the world of programming and data science. With a focus on Python and R, you help students grasp the essentials of data acquisition, analysis, and exploratory techniques. Your role is to provide hints and context, encouraging students to think critically and solve problems independently. You excel in explaining complex concepts simply and offer insights into UNIX command line tools, RDBMS databases, and the fundamentals of machine learning. Your assistance is about nurturing curiosity and understanding, helping students to connect theory with real-world datasets and applications. 
              """,
              model="gpt-4-1106-preview",
            tools=[{"type": "retrieval"}],
            file_ids=[file.id])

    with open(assistant_file_path, 'w') as file:
      json.dump({'assistant_id': assistant.id}, file)
      print("Created a new assistant and saved the ID.")

    assistant_id = assistant.id

  return assistant_id


#   if os.path.exists(assistant_file_path):
#     with open(assistant_file_path, 'r') as file:
#       assistant_data = json.load(file)
#       assistant_id = assistant_data['assistant_id']
#       print("Loaded existing assistant ID.")
#   else:
#     file = client.files.create(file=open("knowledge.docx", "rb"),
#                                purpose='assistants')

#
