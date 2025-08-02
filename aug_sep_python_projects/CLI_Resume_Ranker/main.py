import shutil
import PyPDF2 as pdf
import os
try:
    score=0
    if not os.path.exists('./CLI_Resume_Ranker/Uploads'):
        os.mkdir('./CLI_Resume_Ranker/Uploads')
    keywords = {
        "python": 10,
        "sql": 8,
        "pandas": 7,
        "numpy": 7,
        "data analysis": 10,
        "html": 5,
        "css": 5,
        "javascript": 6,
        "react": 7,
        "node": 6,
        "api": 4,
        "project": 3
    }
    matched=[]
    pdfpath=input('Enter the path of the pdf file:-   ')
    newpath=shutil.move(pdfpath,os.getcwd()+'\\aug_sep_python_projects\\CLI_Resume_Ranker\\Uploads')
    print('Successfully uploaded the file in the server!!!')
    allpages=pdf.PdfReader(newpath)
    text=''
    for pages in allpages.pages:
        text+=pages.extract_text()
    text=text.split(' ')
    for i in text:
        for j in keywords.keys():
            if j.lower() ==i.lower():
                score+=keywords[j]
                matched.append(j)
    matched=list(set(matched))
    print('Total score:-    ',score)

    print('Missing keywords:-   ')
    for i in keywords.keys():
        if i in matched:
            continue
        else:
            print(i)
except Exception as e:
    print(e)
