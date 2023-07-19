def check_fitness(student, profession):
    """Функция получив имя студента и профессию получает словарь с разницей навыков и процент пригодности"""

    students = load_students()
    professions = load_professions()
    for stud in students:
        if student == stud["full_name"]:
            stud_set = set(stud["skills"])
    for prof in professions:
        if profession == prof["title"]:
            prof_set = set(prof["skills"])

    has = list(stud_set.intersection(prof_set))
    lacks = list(prof_set.difference(stud_set))
    percent = round(len(has) * 100 / len(prof_set))

    return {
        "has": has,
        "lacks": lacks,
        "fit_percent": percent
    }