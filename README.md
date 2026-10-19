# Orbit Polytech Contracts

Центральный репозиторий Protobuf-контрактов и сгенерированных gRPC-клиентов для микросервисной экосистемы **Orbit AI** (Московский Политех).

## Структура репозитория

- `proto/` — исходные `.proto` файлы контрактов API сервисов.
  - `proto/orbit/auth/v1/auth.proto` — контракт сервиса аутентификации (`AuthService`).
- `gen/go/` — сгенерированный Go-код (Protobuf-структуры и gRPC клиенты/серверы).
- `docs/` — подробные инженерные спецификации и правила взаимодействия сервисов.
  - [`docs/auth-v1.md`](docs/auth-v1.md) — полная спецификация `AuthService` (поведение методов, ротация токенов, модель сессий и коды ошибок).
- `buf.yaml` — конфигурация Buf CLI с версией спецификации `version: v2` (правила линтинга `STANDARD` и детекция breaking changes категории `FILE`).
- `buf.gen.yaml` — шаблон кодогенерации Go через удалённые плагины Buf с закреплёнными версиями.
- `Taskfile.yml` — кроссплатформенные команды автоматизации проверок и генерации.
- `.github/workflows/ci.yml` — конвейер непрерывной интеграции (CI).

## Требования для разработки

- [Go](https://go.dev/) 1.25+ (в модуле закреплены зависимости gRPC v1.84.0 и Protobuf v1.36.12 для устранения известных CVE)
- [Buf CLI](https://buf.build/docs/installation) (v1.50+)
- **Плагины Protobuf для Go** (устанавливаются один раз локально):
  ```bash
  go install google.golang.org/protobuf/cmd/protoc-gen-go@v1.36.5
  go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v1.5.1
  ```
  *Убедитесь, что каталог `$GOPATH/bin` (обычно `~/go/bin` на Linux/macOS или `%USERPROFILE%\go\bin` на Windows) добавлен в системную переменную `PATH`.*
- [Task](https://taskfile.dev/) (опционально, для удобного запуска задач)
- *Для Windows:* для работы команды `buf format` требуется утилита `diff` (поставляется вместе с Git в каталоге `<GitInstallPath>\usr\bin`, например `F:\Soft\Git\usr\bin` или `C:\Program Files\Git\usr\bin`, который должен быть доступен в `PATH`).

## Спецификация контрактов

Полное описание семантики методов, жизненного цикла OTP-кодов, ротации токенов (Token Family Rotation), идемпотентности и таблицы кодов ошибок gRPC вынесено в отдельный документ:
👉 **[Спецификация AuthService v1](docs/auth-v1.md)**

## Локальная разработка

### Использование Taskfile (рекомендуется)

```bash
# Проверка соответствия proto-файлов стандартам
task lint

# Проверка форматирования
task format-check

# Автоматическое форматирование proto-файлов
task format

# Генерация Go-кода и проверка сборки
task generate

# Полная проверка перед коммитом (lint + format + generate + drift check)
task check
```

### Прямые команды без Task (PowerShell / Windows)

```powershell
# Линтинг
buf lint

# Форматирование
buf format -w

# Чистая генерация Go-кода и сборка
if (Test-Path gen/go) { Remove-Item -Recurse -Force gen/go }
buf generate
go mod tidy
go build ./gen/go/...

# Проверка отсутствия расхождений (drift check)
if (git status --porcelain go.mod go.sum gen/go) {
    Write-Error "Обнаружены незакоммиченные расхождения в go.mod, go.sum или gen/go!"
    exit 1
}
```

## Проверка обратной совместимости (Breaking Changes)

В CI настроена автоматическая проверка совместимости `buf breaking`. 
При первой инициализации репозитория (первый PR) проверка автоматически пропускается, так как в ветке `main` ещё нет схемы для сравнения. Во всех последующих PR будет строго контролироваться обратная совместимость API.

## Подключение в Go-сервисы

Для использования контрактов в микросервисах экосистемы:

```bash
go get github.com/orbit-polytech/contracts
```

Импорт пакета в Go-коде:

```go
import authv1 "github.com/orbit-polytech/contracts/gen/go/orbit/auth/v1"
```
