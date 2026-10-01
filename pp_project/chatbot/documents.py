# 0921-2026
import os
from pathlib import Path
from pypdf import  PdfReader
from django.conf import settings

# Documents and system prompt

data_path = settings.BASE_DIR / "chatbot" / "data"
print(f'data_path: {data_path}')
# Iterate over each file
def load_documents(directory = data_path ):
    documents = []
    for file_path in Path(directory).rglob('*'):
        if file_path.suffix in {'.txt', '.pdf','.md'}:
            if file_path.suffix == '.pdf':
                reader = PdfReader(file_path)
                content = "\n".join(page.extract_text() for page in reader.pages)
                # print(content)
            else:
                content = file_path.read_text(encoding="utf-8")

            documents.append({
                'path': str(file_path),
                'content' : content
            })
    return create_context(documents)

# documents = load_documents()
# print(documents)

def create_context(document_list):
    context =''
    for doc in document_list:
        context = context + f'_______{doc['path']}______\n{doc['content']}\n______________\n'
    return context

# context = create_context(documents)
# print(context)





    # Append the user query to messages ***
    # -- as a HumanMessage to the Messages
    # messages.append(HumanMessage(content=user_query))