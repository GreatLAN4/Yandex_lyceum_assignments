from docxtpl import DocxTemplate


def create_training_sheet(G_class_name, G_subject_name, pl_name, *marks):
    doc = DocxTemplate(str(pl_name))
    marks = sorted(marks, key=lambda x: x[0])

    context = {
        "class_name": G_class_name, "subject_name": G_subject_name,
        'marks': [{'num': i + 1, 'fio': marks[i][0], 'mark': marks[i][1]}
                  for i in range(len(marks))]
    }
    doc.render(context)
    doc.save("res.docx")
