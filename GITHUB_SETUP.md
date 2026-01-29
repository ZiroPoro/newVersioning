# Инструкции по настройке GitHub репозитория

Этот файл содержит инструкции по выполнению оставшихся шагов задания на GitHub.

## Шаги для выполнения

### 1. Создание репозитория на GitHub

1. Перейдите на https://github.com
2. Нажмите кнопку "New repository"
3. Назовите репозиторий (например, `task-manager`)
4. **ВАЖНО**: Не инициализируйте репозиторий с README, .gitignore или лицензией
5. Создайте репозиторий

### 2. Подключение локального репозитория к GitHub

```bash
git remote add origin https://github.com/ВАШ_USERNAME/task-manager.git
git push -u origin master
git push origin develop
git push origin feature/add-task-export
git push --tags
```

### 3. Создание Issues (задач)

Создайте несколько issues в репозитории:

1. Перейдите на вкладку "Issues" в репозитории
2. Нажмите "New issue"
3. Создайте issues для:
   - Добавление новой функции (например, "Add task categories")
   - Исправление бага (например, "Fix task ID generation")
   - Улучшение (например, "Improve user interface")
   - Документация (например, "Update installation guide")

**Примеры названий issues:**
- `Add task categories feature`
- `Fix task ID generation bug`
- `Improve error messages`
- `Add unit tests`

### 4. Настройка Labels (лейблов)

1. Перейдите в Settings → Labels
2. Создайте следующие лейблы:
   - `feature` (зеленый цвет) - для feature веток
   - `hotfix` (красный цвет) - для hotfix веток
   - `bug` (красный цвет)
   - `enhancement` (синий цвет)
   - `documentation` (желтый цвет)

### 5. Использование Labels при мерже

При создании Pull Request или при мерже веток:
- Для feature веток используйте лейбл `feature`
- Для hotfix веток используйте лейбл `hotfix`

### 6. Создание Wiki

1. Перейдите на вкладку "Wiki" в репозитории
2. Нажмите "Create the first page"
3. Создайте следующие страницы:

#### Главная страница (Home)
```
# Task Manager

Task Manager is a simple command-line application for managing daily tasks.

## Navigation
- [About the Program](About-the-Program)
- [What it does](What-it-does)
- [Developer](Developer)
- [Tasks](Tasks)
```

#### About the Program
```
# About the Program

Task Manager is a command-line application developed as part of the DevSecOps course. It provides a simple and efficient way to manage your daily tasks through an intuitive command-line interface.

The application is written in Python and follows best practices for code organization and version control.
```

#### What it does
```
# What it does

Task Manager allows you to:

- Add new tasks with descriptions and priorities
- List all tasks with filtering options
- Mark tasks as completed
- Remove tasks from the list
- Export tasks to a file

The application supports task priorities (low, medium, high) and filtering by completion status and priority level.
```

#### Developer
```
# Developer

This project is developed as part of the DevSecOps course assignment.

**Developer:** [Ваше имя]
**Course:** DevSecOps
**Institution:** [Название учебного заведения]
**GitHub:** [Ваш GitHub профиль]
```

#### Tasks
```
# Tasks

This section contains a list of tasks/issues for the project:

1. [Issue #1: Add task categories feature](https://github.com/username/task-manager/issues/1)
2. [Issue #2: Fix task ID generation bug](https://github.com/username/task-manager/issues/2)
3. [Issue #3: Improve error messages](https://github.com/username/task-manager/issues/3)
4. [Issue #4: Add unit tests](https://github.com/username/task-manager/issues/4)

*(Добавьте ссылки на ваши issues)*
```

### 7. Добавление логотипа

1. Создайте изображение логотипа (можно использовать онлайн генераторы ASCII art или создать простое изображение)
2. Сохраните как `logo.png` или `logo.jpg`
3. Добавьте в репозиторий:
```bash
git add logo.png
git commit -m "Add project logo"
git push origin master
```

4. Обновите README.md, чтобы ссылка указывала на правильный файл

### 8. Создание скриншота Network

1. Перейдите на вкладку "Network" в репозитории GitHub
2. Сделайте скриншот схемы ветвления (убедитесь, что видна вся структура)
3. Сохраните скриншот как `network-diagram.png`
4. Добавьте в репозиторий:
```bash
git add network-diagram.png
git commit -m "Add network branching diagram"
git push origin master
```

5. Убедитесь, что в README.md есть ссылка на этот скриншот

### 9. Создание форка

1. Создайте новый репозиторий на GitHub (например, `task-manager-fork`)
2. Склонируйте основной репозиторий:
```bash
git clone https://github.com/ВАШ_USERNAME/task-manager.git task-manager-fork
cd task-manager-fork
```

3. Измените remote:
```bash
git remote set-url origin https://github.com/ВАШ_USERNAME/task-manager-fork.git
git push -u origin master
git push origin develop
git push origin feature/add-task-export
git push --tags
```

### 10. Обновление резюме

1. Добавьте в ваше резюме (LinkedIn, GitHub профиль и т.д.) блок:
```
## Git Flow & GitHub Experience

Successfully completed Git Flow branching workflow project. Confidently use GitHub for version control, issue tracking, and collaborative development.

Project: [ссылка на репозиторий]
```

2. Добавьте ссылку на резюме в ваш GitHub профиль (в разделе "Website" или в bio)

## Важные напоминания

- ✅ Все названия веток и коммитов только на английском языке
- ✅ Используйте семантическое версионирование (1.0.0, 1.0.1, 1.1.0 и т.д.)
- ✅ Указывайте лейблы при создании Pull Request
- ✅ Удаляйте feature ветки после мержа (кроме последней)
- ✅ Ведите CHANGELOG при каждом мерже
- ✅ Начальная ветка - master (не main)

## Проверка перед сдачей

- [ ] Все файлы созданы (README.md, CHANGELOG.md, install.md, git-commands.md)
- [ ] Репозиторий создан на GitHub
- [ ] Все ветки запушены
- [ ] Созданы issues
- [ ] Настроены лейблы
- [ ] Создана Wiki со всеми разделами
- [ ] Добавлен логотип
- [ ] Добавлен скриншот Network
- [ ] Создан форк
- [ ] Обновлено резюме

