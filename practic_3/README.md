
# Практическая работа №3: Настройка CI/CD для микросервиса

## Описание
В данной практической работе был реализован **CI/CD пайплайн** для автоматизации процесса тестирования, сборки и развертывания микросервиса. Пайплайн построен с использованием **GitHub Actions**, и включает этапы:

- Линтинг кода (`flake8`).
- Сборка Docker-образа и публикация в **Docker Hub**.
- Отправка уведомлений по email при завершении пайплайна.


## Цель работы
1. Изучить и реализовать основные идеи **Continuous Integration (CI)** и **Continuous Deployment (CD)**.  
2. Автоматизировать процесс тестирования, сборки и развертывания микросервиса.  
3. Настроить уведомления о завершении пайплайна.


## Структура репозитория

```plaintext
practic_3/
├── Dockerfile              # Инструкция для сборки Docker-образа
├── main.py                 # Исходный код микросервиса на FastAPI
├── requirements.txt        # Зависимости Python
.github/
└── workflows/
    └── pipeline.yml        # Файл с настройками CI/CD пайплайна
```



## Основные этапы CI/CD пайплайна

###  **Линтинг (Code Linting)**
- Проверка качества кода с использованием `flake8`.
- Пайплайн запускается на каждый `push` и `pull_request` в ветку `main`.

```yaml
- name: Run Linter
  run: flake8 practic_1/main.py practic_2/main.py practic_3/main.py
```



### **Сборка и публикация Docker-образа**
- Сборка Docker-образа с использованием `Dockerfile` из `practic_3`.
- Публикация образа в **Docker Hub**.

```yaml
- name: Build Docker Image
  run: docker build -t ${{ secrets.DOCKERHUB_USERNAME }}/microservice:latest -f practic_3/Dockerfile practic_3/

- name: Push Docker Image
  run: docker push ${{ secrets.DOCKERHUB_USERNAME }}/microservice:latest
```



### **Уведомление по email**
- Отправка уведомления на почту после успешного завершения пайплайна.

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



## Настройка секретов GitHub

Чтобы пайплайн успешно работал, необходимо добавить секретные переменные в **Settings → Secrets and Variables → Actions**:

| **Имя секрета**      | **Описание** |
|----------------------|--------------|
| `DOCKERHUB_USERNAME` | Логин от Docker Hub |
| `DOCKERHUB_PASSWORD` | Пароль от Docker Hub |
| `EMAIL_USERNAME`     | Email для отправки уведомлений (например, `your-email@gmail.com`) |
| `EMAIL_PASSWORD`     | Пароль или **App Password** для авторизации через SMTP |



## Пример использования Docker-образа
После публикации образа, его можно использовать локально:

```bash
docker pull $DOCKERHUB_USERNAME/microservice:latest
docker run -d -p 8000:8000 $DOCKERHUB_USERNAME/microservice:latest
```

Микросервис будет доступен по адресу:
```
http://localhost:8000
```

Swagger-документация доступна по адресу:
```
http://localhost:8000/docs
```



##  Используемый стек технологий
- **FastAPI** — Python-фреймворк для создания API.  
- **Docker** — контейнеризация приложения.  
- **GitHub Actions** — автоматизация CI/CD процессов.  
- **Flake8** — линтинг Python-кода.  
- **SMTP (Gmail)** — отправка уведомлений по email.



##  Пример работы пайплайна
1. **Коммит в ветку `main`**.  
2. GitHub Actions автоматически запускает пайплайн:  
   - Проверяется качество кода (`flake8`).  
   - Собирается Docker-образ и публикуется в Docker Hub.  
   - После успешной сборки отправляется email-уведомление.



##  Особенности и выводы
- Пайплайн CI/CD полностью автоматизирован и запускается на каждый `push` и `pull_request`.  
- В случае успешного завершения, отправляется уведомление на почту.  
- Все секреты (Docker и почта) защищены через GitHub Secrets.  
- Пайплайн легко модифицировать и расширять при необходимости.

