
# Практические работы №1, №2, №3: Контейнеризация, Базы данных и CI/CD

## Описание
Этот проект состоит из трех практических работ, каждая из которых последовательно раскрывает аспекты разработки, контейнеризации, работы с базами данных и автоматизации развертывания микросервисов.

---

# Практическая работа №1: Контейнеризация микросервисного приложения

## Цель работы
- Изучить и реализовать процесс контейнеризации микросервисного приложения.  
- Создать `Dockerfile` для сборки Docker-образа.  
- Настроить микросервис с использованием `FastAPI` и `SQLite`.

---

## Структура проекта
```plaintext
practic_1/
├── Dockerfile              # Инструкция для сборки Docker-образа
├── main.py                 # Исходный код микросервиса на FastAPI
├── requirements.txt        # Зависимости Python
```

---

## Основные этапы работы
1. **Разработка микросервиса** с использованием FastAPI.  
2. **Создание `Dockerfile`** для упаковки микросервиса.  
3. **Сборка Docker-образа** и тестирование его локально.  
4. **Swagger UI** доступен по адресу `/docs`.

---

## Запуск микросервиса
```bash
docker build -t microservice:latest .
docker run -d -p 8000:8000 microservice:latest
```

Микросервис будет доступен по адресу:
```
http://localhost:8000
```

---

# Практическая работа №2: Развертывание базы данных в Minikube

## Цель работы
- Изучить принципы работы с базами данных в микросервисной архитектуре.  
- Развернуть PostgreSQL в Minikube.  
- Настроить подключение микросервиса к базе данных.

---

## Структура проекта
```plaintext
practic_2/
├── kubernetes/
│   ├── postgres-deployment.yaml     # Развертывание базы данных
│   └── postgres-service.yaml        # Сервис для доступа к БД
├── main.py                          # Код для тестирования подключения к БД
```

---

## Основные этапы работы
1. Развертывание **PostgreSQL** в Minikube.  
2. Настройка подключения к базе данных через SQLAlchemy.  
3. Создание тестовых данных и проверка работы запросов.

---

## Команды для запуска
```bash
kubectl apply -f kubernetes/postgres-deployment.yaml
kubectl apply -f kubernetes/postgres-service.yaml
kubectl port-forward svc/postgres 5432:5432
```

- Подключение к базе данных:
```bash
psql -h localhost -U user -d microservice_db
```

---

# Практическая работа №3: CI/CD для микросервиса

## Цель работы
- Настроить полноценный CI/CD-процесс с использованием GitHub Actions.  
- Автоматизировать процесс тестирования, сборки, публикации Docker-образа и отправки уведомлений.

---

## Структура проекта
```plaintext
practic_3/
├── Dockerfile              # Инструкция для сборки Docker-образа
├── main.py                 # Исходный код микросервиса
├── requirements.txt        # Зависимости Python
.github/
└── workflows/
    └── pipeline.yml        # Настройка CI/CD пайплайна
```

---

## Основные этапы CI/CD пайплайна

### **Линтинг (Code Linting)**
- Проверка кода с использованием `flake8`.

```yaml
- name: Run Linter
  run: flake8 practic_1/main.py practic_2/main.py practic_3/main.py
```

---

### **Сборка и публикация Docker-образа**
- Сборка образа и его публикация в **Docker Hub**.

```yaml
- name: Build Docker Image
  run: docker build -t ${{ secrets.DOCKERHUB_USERNAME }}/microservice:latest -f practic_3/Dockerfile practic_3/

- name: Push Docker Image
  run: docker push ${{ secrets.DOCKERHUB_USERNAME }}/microservice:latest
```

---

### **Уведомление по email**
- Отправка уведомления о завершении пайплайна.

```yaml
- name: Send email
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 587
    username: ${{ secrets.EMAIL_USERNAME }}
    password: ${{ secrets.EMAIL_PASSWORD }}
    subject: "CI/CD Pipeline Completed"
    body: "CI/CD Pipeline успешно завершен!"
    to: "your-email@example.com"
    from: "GitHub Actions"
```

---

### Настройка секретов GitHub

Добавьте следующие секреты в **Settings → Secrets and Variables → Actions**:

| **Имя секрета**      | **Описание** |
|----------------------|--------------|
| `DOCKERHUB_USERNAME` | Логин от Docker Hub |
| `DOCKERHUB_PASSWORD` | Пароль от Docker Hub |
| `EMAIL_USERNAME`     | Email для отправки уведомлений |
| `EMAIL_PASSWORD`     | Пароль или App Password для SMTP |

---

## Выбор метода ветвления

**Выбранный метод:** `GitHub Flow`

### Почему выбран `GitHub Flow`:
- Простота и гибкость.
- Оптимален для CI/CD процессов.
- Минимум конфликтов и простота интеграции.

### Как работает:
1. Создается ветка для каждой новой фичи.
2. Изменения отправляются в PR.
3. Пайплайн запускается автоматически и тестирует изменения.
4. После успешного теста — PR вливается в `main`.

---

## Выводы
- Построен полный цикл разработки микросервиса с его контейнеризацией, развертыванием базы данных и автоматизацией CI/CD.  
- Настроен полный процесс тестирования, сборки и публикации с уведомлением о завершении.

---
