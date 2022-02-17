def person_information(name, lastname, year_of_birth, city, email, phone_number):
    return print(f'Имя -  {name}  Фамилия - {lastname}  Год рождения - {year_of_birth} Город проживания - {city}  Email - {email}  Телефон - {phone_number}')


person_information(
    name=input('Введите имя: '),
    lastname=input('Введите фамилию: '),
    year_of_birth= int(input('Введите год рождения:  ')),
    city=input('Введите город проживания: '),
    email=input('Введите email: '),
    phone_number=input('Введите номер телефона: '),
)
