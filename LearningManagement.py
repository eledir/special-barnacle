import os

# Definizione della struttura
base_dir = "LearningManagement"
templates_dir = os.path.join(base_dir, "templates")
files = [
    "assignment_detail.html",
    "assignment_form.html",
    "course_detail.html",
    "course_list.html",
    "course_form.html",
    "dashboard_admin.html",
    "dashboard_student.html",
    "dashboard_teacher.html",
    "submission_form.html",
    "submission_list.html",
]

# Creazione cartelle
os.makedirs(templates_dir, exist_ok=True)

# Creazione file
for file in files:
    file_path = os.path.join(templates_dir, file)
    with open(file_path, "w") as f:
        f.write(f"<!-- {file} template -->\n")

print("✅ Struttura LMS creata con successo!")
