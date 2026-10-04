# Тест-дизайн формы регистрации Steam

## Параметры и значения
- Email: валидный / невалидный / пустой
- Reenter email: совпадает / не совпадает / пустой
- Капча: пройдена / не пройдена
- Согласие: отмечено / не отмечено

## Классы эквивалентности для email
- Валидные: test@example.com, user.name@domain.co
- Невалидные: без @, без домена, с пробелом, пустой
- Граничные: максимальная длина, минимальная длина

## Попарное тестирование (pairwise)

| # | Email | Reenter | Капча | Согласие |
|---|---|---|---|---|---|
| 1 | test_user@gmail.com | test_user@gmail.com | True | True |
| 2 | test_user@gmail.com | new_user@gmail.com | False | False |
| 3 | test_user@gmail.com | "" | True | True |
| 4 | test_user@@gmail.com | test_user@@gmail.com | False | False |
| 5 | .testuser@gmail.com | .newuser@gmail.com | True | True |
| 6 | test_user@gmailcom | "" | False | False |
| 7 | "" | test_user@gmail.com | True | False |
| 8 | "" | "" | False | True |

Страна всегда выбрана поэтому является константой, поэтому не отображается в таблице для составления пар.

...

## Выводы
Попарное тестирование сократило количество тестов с 81 до 8,
покрыв все пары параметров.
