from resume_parser import resumeparse
import docx2txt


def fin(DocxResume):
    resume = docx2txt.process(DocxResume)

    file_name = DocxResume
    
    data = resumeparse.read_file(file_name)
    return data
  #  for i in data.items():
   #     print(i[0],":",i[1])
