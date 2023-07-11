from decorators import printable_view
from dto import Student, Profession


@printable_view(as_string=True)
def check_fitness(student: Student, profession: Profession):
    """
    Проверяет соответствие студента профессии по соответсвующим
    атрибутам моделей.

    Parameters
    ----------
    student : экземляр модели Student
    profession : экземляр модели Profession

    Returns
    -------
    Словарь со статистикой соответствия студента профессии.
    """

    has = set(student.skills) & set(profession.skills)
    lacks = set(profession.skills) - set(student.skills)
    fit_percent = round(
        (len(has) / len(profession.skills)) * 100
    )

    return {
        "has": has,
        "lacks": lacks,
        "fit_percent": fit_percent,
    }


def main():
    student_search_term = input(
        "Введите номер студента\n"
    )

    if student := Student.get(pk=student_search_term):
        print(f"Студент {student}\n"
              f"Знает {student.skills_}")
    else:
        print("У нас нет такого студента")
        return

    prof_search_term = input(
        f"Выберите специальность для оценки студента {student}\n"
    )

    if profession := Profession.get(title=prof_search_term):
        print("%s\n" % profession)
    else:
        print("У нас нет такой специальности")
        return

    print(check_fitness(student=student, profession=profession))


if __name__ == "__main__":
    main()
