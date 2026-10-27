# Orbit Polytech Contracts

Центральный репозиторий Protobuf-контрактов и сгенерированных gRPC-клиентов для микросервисной экосистемы **Orbit Polytech** (Московский Политех).

## Структура репозитория

- `proto/` — исходные `.proto` файлы контрактов API сервисов:
  - `proto/orbit/auth/v1/auth.proto` — сервис аутентификации (`AuthService`).
  - `proto/orbit/schedule/v1/schedule.proto` — сервис расписания занятий (`ScheduleService`).
  - `proto/orbit/ai/v1/ai.proto` — сервис искусственного интеллекта и стриминга ответов (`AIService`).
- `gen/go/` — сгенерированный Go-код (Protobuf-структуры и gRPC клиенты/серверы).
- `gen/python/` — сгенерированный Python-код (Protobuf-сообщения и gRPC stubs).
- `docs/` — подробные инженерные спецификации и правила взаимодействия сервисов:
  - [`docs/auth-v1.md`](docs/auth-v1.md) — спецификация `AuthService` (сессии, ротация токенов, OTP, коды ошибок).
  - [`docs/schedule-v1.md`](docs/schedule-v1.md) — спецификация `ScheduleService` (кэширование, Stale-While-Revalidate, инварианты дат).
  - [`docs/ai-v1.md`](docs/ai-v1.md) — спецификация `AIService` (жизненный цикл стриминга, стадии, идемпотентность, отмена генерации).
- `buf.yaml` — конфигурация Buf CLI (`version: v2`, стандарты линтинга `STANDARD`, контроль breaking changes).
- `buf.gen.yaml` — конфигурация кодогенерации Go и Python через закреплённые удалённые плагины Buf.
- `Taskfile.yml` — кроссплатформенные команды автоматизации проверок и генерации.
- `.github/workflows/ci.yml` — конвейер непрерывной интеграции (CI) с проверками Go и Python.

---

## Требования для разработки

### Общие
- [Buf CLI](https://buf.build/docs/installation) (v1.50+)
- [Git](https://git-scm.com/)

### Для сборки Go
- [Go](https://go.dev/) 1.25+
- **Плагины Protobuf для Go** (устанавливаются один раз):
  ```bash
  go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.36.5
  go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.5.1
  ```
  *Убедитесь, что каталог `$GOPATH/bin` добавлен в системную переменную `PATH`.*

### Для проверки и запуска Python
- [Python](https://www.python.org/) 3.12+ или менеджер пакетов [uv](https://docs.astral.sh/uv/)
- **Закреплённые runtime-зависимости:**
  ```bash
  pip install "protobuf>=5.28,<6" "grpcio>=1.68,<2"
  ```

### Особенности Windows
Для выполнения команды `buf format -d` (проверка форматирования без перезаписи) требуется стандартная утилита `diff`. На Windows она устанавливается вместе с Git и находится в каталоге `<GitInstallPath>\usr\bin` (например, `C:\Program Files\Git\usr\bin` или пользовательский путь установки Git). Этот путь должен быть добавлен в системную переменную `PATH`.

---

## Инженерные спецификации сервисов

Подробное описание семантики методов, жизненного цикла запросов, идемпотентности и кодов ошибок:
- 👉 [Спецификация AuthService v1](docs/auth-v1.md)
- 👉 [Спецификация ScheduleService v1](docs/schedule-v1.md)
- 👉 [Спецификация AIService v1](docs/ai-v1.md)

---

## Локальная разработка

### Использование Taskfile (рекомендуется)

```bash
# Проверка соответствия proto-файлов стандартам
task lint

# Проверка форматирования
task format-check

# Автоматическое форматирование proto-файлов
task format

# Генерация кода для Go и Python с последующей верификацией сборки Go
task generate

# Полная проверка перед коммитом (lint + format + generate + drift check)
task check
```

### Прямые команды без Task (PowerShell / Bash)

```bash
# Линтинг
buf lint

# Форматирование proto-файлов
buf format -w

# Чистая генерация Go и Python
rm -rf gen/go gen/python
buf generate
go mod tidy
go build ./gen/go/...

# Проверка отсутствия расхождений (drift check)
git status --porcelain go.mod go.sum gen/go gen/python
```

---

## Проверка Python-модулей (Smoke Test)

Для быстрой проверки корректности импортов и сериализации сообщений всех сгенерированных пакетов:

```bash
python -c "
import sys
sys.path.insert(0, 'gen/python')
from orbit.ai.v1 import ai_pb2, ai_pb2_grpc
from orbit.auth.v1 import auth_pb2, auth_pb2_grpc
from orbit.schedule.v1 import schedule_pb2, schedule_pb2_grpc

req = ai_pb2.ChatStreamRequest(query='Тест')
assert req.query == 'Тест'
print('Все Python-пакеты успешно проверены')
"
```

---

## Подключение контрактов в микросервисы

### В Go-сервисы (`auth-service`, `schedule-service`, `gateway-service`)

Установка модуля:
```bash
go get github.com/orbit-polytech/contracts
```

Импорт в Go-коде:
```go
import (
    authv1 "github.com/orbit-polytech/contracts/gen/go/orbit/auth/v1"
    schedulev1 "github.com/orbit-polytech/contracts/gen/go/orbit/schedule/v1"
    aiv1 "github.com/orbit-polytech/contracts/gen/go/orbit/ai/v1"
)
```

### В Python-сервисы (`ai-service`)

В локальной разработке монорепозитория/полирепозитория пакет подключается через `pyproject.toml` микросервиса:

```toml
[tool.uv.sources]
orbit-contracts = { path = "../contracts/gen/python", editable = true }
```

Либо через прямое добавление пути в виртуальное окружение:
```bash
pip install -e ../contracts/gen/python
```

Импорт в коде сервиса:
```python
from orbit.ai.v1 import ai_pb2, ai_pb2_grpc
```
