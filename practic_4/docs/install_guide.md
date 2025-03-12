# Руководство по установке

## Описание
В этом руководстве представлены инструкции по установке и запуску программного продукта.

---

## Требования к системе

- **Операционная система:** Windows/Linux/macOS  
- **Python:** версии 3.9 и выше  
- **Docker:** для контейнеризации приложения  
- **Minikube:** для локального развертывания Kubernetes (если требуется)

---

## Установка зависимостей

1. **Клонирование репозитория**
```bash
git clone https://github.com/nik231097/2023_2025-application_containerization_and_orchestration-k4112_Solodovnikov.git
cd project-repo
```

2. **Создание виртуального окружения**
```bash
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\\Scripts\\activate   # Для Windows
```

3. **Установка зависимостей**
```bash
pip install -r requirements.txt
```


## Запуск с помощью Docker

1. **Сборка Docker-образа**
```bash
docker build -t microservice:latest .
```

2. **Запуск Docker-контейнера**
```bash
docker run -d -p 8000:8000 microservice:latest
```

Приложение будет доступно по адресу:
```
http://localhost:8000
```


## Установка PostgreSQL в Minikube (если используется база данных)

1. **Запуск Minikube**
```bash
minikube start
```

2. **Применение манифестов Kubernetes**
```bash
kubectl apply -f kubernetes/postgres-deployment.yaml
kubectl apply -f kubernetes/postgres-service.yaml
```

3. **Проброс порта**
```bash
kubectl port-forward svc/postgres 5432:5432
```

4. **Подключение к базе данных**
```bash
psql -h localhost -U user -d microservice_db
```



## Проверка установки

1. Перейдите по адресу:
```
http://localhost:8000
```

2. Проверьте, что приложение запускается корректно.  
3. Для проверки API перейдите в документацию Swagger:
```
http://localhost:8000/docs
```


## Возможные ошибки

- **Ошибка подключения к базе данных**  
  Убедитесь, что база данных запущена и правильно настроены параметры подключения.

- **Ошибка при сборке Docker-образа**  
  Проверьте `Dockerfile` на наличие синтаксических ошибок.
