import pandas as pd

dfs = pd.read_html('http://attendance.mec.ac.in/view4stud.php?class=C6A&submit=view', attrs = {'class':'attn'})

dfs[0][2:].to_csv('output.csv', index=False, header=['Roll No', 'Name', 'Design & Analysis of Algorithms','Compiler Design', 'Computer Networks', 'Software Engineering & Project Management', 'Comprehensive Exam', ' Principles of Management', 'Microprocessor Lab', 'Network Programming Lab', 'Natural Language Processing', 'Web Technologies'])
