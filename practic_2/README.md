
#  Практическая работа №2: Развертывание базы данных в Minikube

##  Описание
В данной работе была развернута база данных PostgreSQL в Minikube и настроено подключение микросервиса к базе данных.

---

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
└── img/                             # Папка для изображений
```

---

## Папка с изображениями
Все скриншоты и иллюстрации, относящиеся ко второй практической работе, находятся в папке [`img`](./img).

---

## Основные этапы работы

###  Развертывание PostgreSQL в Minikube
```bash
kubectl apply -f kubernetes/postgres-deployment.yaml
kubectl apply -f kubernetes/postgres-service.yaml
```

### Проброс порта для доступа к базе
```bash
kubectl port-forward svc/postgres 5432:5432
```

### Подключение к базе данных
```bash
psql -h localhost -U user -d microservice_db
```

---

##  Пример `postgres-deployment.yaml`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:latest
        env:
        - name: POSTGRES_USER
          value: "user"
        - name: POSTGRES_PASSWORD
          value: "password"
        - name: POSTGRES_DB
          value: "microservice_db"
        ports:
        - containerPort: 5432
```

---

## Пример `postgres-service.yaml`

```yaml
apiVersion: v1
kind: Service
metadata:
  name: postgres
spec:
  selector:
    app: postgres
  ports:
  - protocol: TCP
    port: 5432
    targetPort: 5432
  type: ClusterIP
```

---

##  Проверка работы приложения

- После подключения к базе, создаем таблицу:

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
```

- Добавляем тестовые данные:

```sql
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com');
```

- Проверяем данные:

```sql
SELECT * FROM users;
```

---

## Используемый стек технологий

- **PostgreSQL** — реляционная база данных.  
- **Minikube** — локальное развертывание Kubernetes.  
- **kubectl** — CLI для управления Kubernetes.  
- **psql** — CLI для управления PostgreSQL.

---

## Выводы
- Успешно развернута база данных PostgreSQL в Minikube.  
- Установлено и проверено подключение к базе данных.  
- Данные успешно добавлены и считаны через SQL-запросы.

