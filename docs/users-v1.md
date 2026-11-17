# Спецификация контракта UserService (v1)

Документ фиксирует структуру данных и методы gRPC-сервиса профилей пользователей (`orbit.users.v1.UserService`) экосистемы **Orbit Polytech**.

Контракт Protobuf:
- [`proto/orbit/users/v1/users.proto`](../proto/orbit/users/v1/users.proto) — сервис и модели профиля пользователя

---

## 1. Обзор

`UserService` предоставляет чтение, создание/обновление и пакетное получение профилей пользователей по идентификатору аккаунта (`account_id`).

---

## 2. Сущности и перечисления

### `UserRole`
| Значение | Код | Описание |
| :--- | :--- | :--- |
| `USER_ROLE_UNSPECIFIED` | `0` | Значение по умолчанию Protobuf |
| `USER_ROLE_STUDENT` | `1` | Студент |
| `USER_ROLE_TEACHER` | `2` | Преподаватель |
| `USER_ROLE_ADMIN` | `3` | Администратор |

### `UserProfile`
| Поле | Тип | Описание |
| :--- | :--- | :--- |
| `id` | `string` | Идентификатор профиля |
| `account_id` | `string` | Идентификатор аккаунта из `AuthService` |
| `first_name` | `string` | Имя |
| `last_name` | `string` | Фамилия |
| `middle_name` | `string` | Отчество |
| `avatar_url` | `string` | Ссылка на аватар |
| `academic_group` | `string` | Учебная группа |
| `course` | `optional int32` | Номер курса |
| `role` | `UserRole` | Роль пользователя |
| `created_at` | `google.protobuf.Timestamp` | Время создания профиля |
| `updated_at` | `google.protobuf.Timestamp` | Время последнего обновления профиля |

---

## 3. Методы `UserService`

| RPC | Запрос | Ответ | Назначение и семантика |
| :--- | :--- | :--- | :--- |
| `GetProfile` | `GetProfileRequest { account_id }` | `GetProfileResponse { profile }` | Получение профиля пользователя по `account_id`. |
| `UpdateProfile` | `UpdateProfileRequest { account_id, first_name, last_name, middle_name, avatar_url, academic_group, optional course }` | `UpdateProfileResponse { profile }` | Создаёт профиль либо полностью заменяет его редактируемые поля. Пустые необязательные строки и отсутствие `course` очищают соответствующие значения. |
| `GetBatchProfiles` | `GetBatchProfilesRequest { repeated account_ids }` | `GetBatchProfilesResponse { repeated profiles }` | Внутренний метод для пакетного получения профилей по списку `account_ids`; не публикуется как открытый HTTP endpoint. |
