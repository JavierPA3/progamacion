from TercerTrimestre.AutoTest.Question import Question

exam_questions = []
with open("examen.txt", "rt") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 6):
        name = lines[i].strip()
        statement = lines[i + 1].strip()
        choices = [tuple(line.strip().split(",")) for line in lines[i + 2:i + 6]]
        question = Question(name, statement, choices)
        exam_questions.append(question)