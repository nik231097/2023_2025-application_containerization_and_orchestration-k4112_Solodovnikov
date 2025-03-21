# Руководство пользователя

## Описание
Это руководство содержит инструкции по использованию программного продукта, включая описание интерфейсов, доступных функций и пошаговых инструкций.


## Запуск приложения

1. Убедитесь, что приложение установлено и запущено.
2. Откройте веб-браузер и перейдите по адресу:
```
http://localhost:8000
```


## Основной функционал

### **Главная страница**
- При переходе по базовому URL (`/`) отобразится статус работы микросервиса.

### **Создание пользователя**
- Перейдите в Swagger UI по адресу:
```
http://localhost:8000/docs
```
- Выберите `POST /users/` и введите данные нового пользователя:

```json
{
    "name": "Nikolay",
    "email": "nikolay@yandex.ru"
}
```

- Нажмите "Execute", чтобы создать нового пользователя.



### **Просмотр всех пользователей**
- В Swagger UI выберите `GET /users/`.  
- Нажмите "Execute", чтобы получить список всех пользователей.

---

### **Получение пользователя по ID**
- В Swagger UI выберите `GET /users/{id}`.
- Введите `id` пользователя и нажмите "Execute".

---

### **Удаление пользователя**
- В Swagger UI выберите `DELETE /users/{id}`.
- Введите `id` пользователя и нажмите "Execute".

---

## Дополнительные функции

- **Swagger UI:** предоставляет удобный интерфейс для тестирования API.  
- **Автоматическая валидация:** FastAPI автоматически проверяет корректность введенных данных.  

---

## Часто возникающие ошибки

- **400 Bad Request:** некорректный формат данных.  
- **404 Not Found:** пользователь с указанным ID не найден.  
- **500 Internal Server Error:** ошибка на сервере (проверьте логи).

---

## Примеры ошибок

- **Ошибка 400 (некорректный email):**
```json
{
    "detail": "Некорректный формат email-адреса."
}
```

- **Ошибка 404 (пользователь не найден):**
```json
{
    "detail": "Пользователь с указанным ID не найден."
}
```

