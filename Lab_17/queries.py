from sqlalchemy import func
from models import Label, Composition, Musician, Performance
from datetime import date

def run_queries(db):
    #1.Выборка всех композиций и их лейблов
    print("\nВсе композиции и их лейблы:")
    for composition in db.query(Composition).join(Label).all():
        print(f"{composition.title} - {composition.label.label_name}")
    #2.Выборка музыкантов, исполнявших определенную композицию (например, "Bohemian Rhapsody")
    print("\nМузыканты, исполнявшие Bohemian Rhapsody:")
    for musician in db.query(Musician).join(Performance).join(Composition).filter(Composition.title == "Bohemian Rhapsody").all():
        print(musician.musician_name)
    #3.Подсчет количества композиций на каждом лейбле
    print("\nКоличество композиций на каждом лейбле:")
    for label, count in db.query(Label, func.count(Composition.composition_id)).outerjoin(Composition).group_by(Label.label_id).all():
        print(f"{label.label_name}: {count}")
    #4.Выборка композиций, исполненных после определенной даты (например, после 2000 года)
    print("\nКомпозиции, исполненные после 2000 года:")
    for performance in db.query(Performance).filter(Performance.performance_date > date(2000, 1, 1)).join(Composition).all():
        print(f"{performance.composition.title} - {performance.musician.musician_name} ({performance.performance_date})")
    #5.Поиск самого популярного музыканта, судя по количеству исполненных композиций
    print("\nСамый популярный музыкант:")
    most_popular_musician = db.query(Musician, func.count(Performance.composition_id)).join(Performance).group_by(Musician.musician_id).order_by(func.count(Performance.composition_id).desc()).first()
    if most_popular_musician:
        print(f"{most_popular_musician[0].musician_name} - {most_popular_musician[1]} исполнений")
    else:
        print("Нет данных о выступлениях.")