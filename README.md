# Приложение-переводчик
## Приложение на PyQt5, которое переводит фразы с одного языка на другой.
## *Функционал:*
- перевод фраз на другой язык
- голосовой ввод фразы
- функция озвучки текста
- копирование текста
- переключение направление языка
- удаление текста
- считывание содержимого из файла с расширением *.txt
## *Запуск:*
- Установить python версии 3.10+
- Установить все библиотеки, перечисленные в requiremenets.txt файле с помощью (python -m pip install -r ./requirements или pip install -r requirements.txt)
- Запустить игру с помощью команды python main.py
## *Руководство по использованию приложения:*
- В приложении присутствуют две вкладки: «Текст», «Документ».
- Нажав на вкладку «Текст» можно сделать следующее:
•	Ввести фразу на интересующем вас языке и перевести её, нажав на кнопку «Перевести»\
•	Выбрать язык ввода и языка вывода, нажав на соответствующую кнопку. По умолчанию на этих кнопках написано «Выбрать язык». При нажатии на одну из кнопок открывается новое окно с выбором языка. Чтобы выбрать интересующий вас языка, достаточно кликнуть на него\
•	Можно поменять местами языки, нажав на кнопку со стрелками. При смене направления текст в полях для ввода и вывода автоматически удалится\
•	Можно удалить текст в поле для ввода, нажав на крестик\
•	Пользователь может скопировать текст как в поле для ввода, так и в поле для вывода перевода\
•	Есть функция голосового ввода, позволяющая вводить фразу «голосом». Перед использованием этой функции необходимо выбрать язык\
•	Каждое текстовое поле можно озвучить, нажав на значок динамика

- Нажав на вкладку «Текст» можно сделать следующее:
•	Пользователь может загрузить *.txt файл, нажав на кнопку «Загрузить файл»\
•	Выбрать интересующий пользователя язык для перевода\
•	Совершить перевод содержимого файла, нажав на кнопку «Перевести»\
•	Удалить содержимое полей для ввода и вывода фраз, нажав на крестик
- Важно: для правильного перевода документа загружайте файлы, с языком, который есть в окне выбора языка (всего доступно 99 языка).
- Желаем удачного пользования приложением!
