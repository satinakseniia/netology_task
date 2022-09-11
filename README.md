# netology_task

Пример реализации уязвимости injection:

Представлен постой сайт с двумя формами для ввода текста (например, пароль и логин). 
![image](https://user-images.githubusercontent.com/113315420/189552783-b68f9c49-8283-44f1-b163-2140f8dc8c47.png)

После ввода текста введенные данные выводятся на экран.
![image](https://user-images.githubusercontent.com/113315420/189552788-8c8d537f-007c-4a08-bce3-86b6945a0b12.png)

Попробуем вместо текста указать простой скрипт: <script>alert("This is fail")</script>
![image](https://user-images.githubusercontent.com/113315420/189552840-27e3bb74-2215-4be6-a386-d1375e037d50.png)

Получим такой результат
![image](https://user-images.githubusercontent.com/113315420/189552796-20833977-efcf-47eb-b0fe-b15e50d9c1a2.png)


Программа обрабатывает скрипт и выводит ошибку вместо текста. 
При правильной обработке скрипт либо не должен приниматься на вход программы вообще (должна выводиться информация об ошибке - валидация входных данных, либо скрипт должен восприниматься как текст - экранирование символов)

