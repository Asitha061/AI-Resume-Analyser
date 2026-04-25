resume=input("Paste resume:\n")

skills=["python","sql","machine learning","git"]

found=0

for skill in skills:
    if skill in resume.lower():
        found +=1

score=(found/len(skills))*100

print("Resume Match Score:",score,"%")