# 🏋️‍♂️ Gym Tracker Backend

Бэкенд-сервис для VK Mini App, предназначенный для трекинга и планирования тренировок. Пользователи могут записывать тренировки, отслеживать упражнения, подходы и прогресс. Разработано в рамках программы **VK Education Practice**.

---

## ⚙️ Стек технологий

- **Python**, **Django**, **Django REST Framework**
- **Gunicorn** — WSGI-сервер
- **PostgreSQL** (или SQLite)
- **Docker**, **Docker Compose**
- **drf-spectacular** — OpenAPI (Swagger) документация

---

## 🚀 Основной функционал

### 🧠 CRUD для следующих сущностей:

#### 📌 Тренировка (`Workout`)
- Поля: `user`, `date`, `note`, `duration`, `calories_burnt`

#### 📌 Шаблон упражнения (`ExerciseTemplate`)
- Поля: `user`, `name`, `muscle_group`

#### 📌 Упражнение в тренировке (`WorkoutExercise`)
- Поля: `workout`, `template`, `order`

#### 📌 Подход (`Set`)
- Поля: `workout_exercise`, `weight`, `reps`, `duration`, `order`

---

## 🐳 Запуск с Docker

1. **Клонируйте репозиторий:**
```bash
   git clone https://github.com/your-name/gym-tracker-backend.git
   cd gym-tracker-backend
```

2.	Создайте .env файл:
•	Основан на .env.example (если есть)
•	Пример переменных:

```env
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

3.	Соберите образ:
```docker
docker-compose build
```

4.	Запустите контейнеры:
```
docker-compose up -d
```

5.	Выполните миграции:
```
docker-compose exec web python manage.py migrate
```

6.	Приложение будет доступно по адресу:
```
http://localhost:8000
```

## 📡 API Эндпоинты

### 🧩 Шаблоны упражнений /api/templates/

| Метод | Эндпоинт                               | Описание                                  |
|-------|----------------------------------------|-------------------------------------------|
| GET   | /api/templates/                        | Получить список всех шаблонов упражнений  |
| POST  | /api/templates/                        | Создать новый шаблон упражнения           |
| GET   | /api/templates/{template_id}/          | Получить детали шаблона по его ID         |
| PUT   | /api/templates/{template_id}/          | Полностью обновить шаблон                 |
| PATCH | /api/templates/{template_id}/          | Частично обновить шаблон                  |
| DELETE| /api/templates/{template_id}/          | Удалить шаблон                            |

### 🏋️‍♂️ Тренировки /api/workouts/

| Метод | Эндпоинт                               | Описание                                  |
|-------|----------------------------------------|-------------------------------------------|
| GET   | /api/workouts/                         | Получить список всех тренировок           |
| POST  | /api/workouts/                         | Создать новую тренировку                  |
| GET   | /api/workouts/{workout_id}/            | Получить детали тренировки по её ID       |
| PUT   | /api/workouts/{workout_id}/            | Полностью обновить тренировку             |
| PATCH | /api/workouts/{workout_id}/            | Частично обновить тренировку              |
| DELETE| /api/workouts/{workout_id}/            | Удалить тренировку                        |

### 🏃 Упражнения в тренировке /api/workouts/{workout_id}/exercises/

| Метод | Эндпоинт                                                    | Описание                                  |
|-------|-------------------------------------------------------------|-------------------------------------------|
| GET   | /api/workouts/{workout_id}/exercises/                       | Получить список упражнений для тренировки |
| POST  | /api/workouts/{workout_id}/exercises/                       | Создать новое упражнение в тренировке     |
| GET   | /api/workouts/{workout_id}/exercises/{exercise_id}/        | Получить детали упражнения                |
| PUT   | /api/workouts/{workout_id}/exercises/{exercise_id}/        | Полностью обновить упражнение             |
| PATCH | /api/workouts/{workout_id}/exercises/{exercise_id}/        | Частично обновить упражнение              |
| DELETE| /api/workouts/{workout_id}/exercises/{exercise_id}/        | Удалить упражнение                        |

### 🔁 Подходы /api/workouts/{workout_id}/exercises/{exercise_id}/sets/

| Метод | Эндпоинт                                                                 | Описание                                  |
|-------|--------------------------------------------------------------------------|-------------------------------------------|
| GET   | /api/workouts/{workout_id}/exercises/{exercise_id}/sets/                | Получить список подходов для упражнения   |
| POST  | /api/workouts/{workout_id}/exercises/{exercise_id}/sets/                | Создать новый подход                      |
| GET   | /api/workouts/{workout_id}/exercises/{exercise_id}/sets/{set_id}/       | Получить детали подхода                   |
| PUT   | /api/workouts/{workout_id}/exercises/{exercise_id}/sets/{set_id}/       | Полностью обновить подход                 |
| PATCH | /api/workouts/{workout_id}/exercises/{exercise_id}/sets/{set_id}/       | Частично обновить подход                  |
| DELETE| /api/workouts/{workout_id}/exercises/{exercise_id}/sets/{set_id}/       | Удалить подход                            |

### 🔐 Требуется аутентификация для всех запросов


## 🧑‍💻 Разработчик
	•	Автор: Segun228
	•	Лицензия: MIT