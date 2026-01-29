# Следующие шаги для завершения задания

## ✅ Что уже сделано:
- Репозиторий создан на GitHub
- Код загружен
- Ветки созданы (master, develop, feature/add-task-export)
- Теги созданы (v1.0.0, v1.0.1)
- Issues созданы (4 штуки)

## 📋 Что нужно сделать дальше:

### 1. Настроить Labels (лейблы) - ОБЯЗАТЕЛЬНО!

1. В вашем репозитории на GitHub перейдите: **Settings** → **Labels** (или просто нажмите на вкладку Issues, затем справа "Labels")
2. Создайте следующие лейблы:
   - `feature` (зеленый цвет #0e8a16) - для feature веток
   - `hotfix` (красный цвет #d73a4a) - для hotfix веток
   - `bug` (красный цвет #d73a4a)
   - `enhancement` (синий цвет #0052cc)
   - `documentation` (желтый цвет #fbca04)

3. **ВАЖНО**: При создании Pull Request для feature веток - используйте лейбл `feature`, для hotfix - лейбл `hotfix`

### 2. Создать Wiki - ОБЯЗАТЕЛЬНО!

1. В репозитории нажмите на вкладку **Wiki**
2. Нажмите "Create the first page"
3. Создайте следующие страницы:

#### Главная страница (Home):
```markdown
# Task Manager

Task Manager is a simple command-line application for managing daily tasks.

## Navigation
- [About the Program](About-the-Program)
- [What it does](What-it-does)
- [Developer](Developer)
- [Tasks](Tasks)
```

#### Страница "About the Program":
```markdown
# About the Program

Task Manager is a command-line application developed as part of the DevSecOps course. It provides a simple and efficient way to manage your daily tasks through an intuitive command-line interface.

The application is written in Python and follows best practices for code organization and version control.
```

#### Страница "What it does":
```markdown
# What it does

Task Manager allows you to:

- Add new tasks with descriptions and priorities
- List all tasks with filtering options
- Mark tasks as completed
- Remove tasks from the list
- Export tasks to a file

The application supports task priorities (low, medium, high) and filtering by completion status and priority level.
```

#### Страница "Developer":
```markdown
# Developer

This project is developed as part of the DevSecOps course assignment.

**Developer:** [Ваше имя]
**Course:** DevSecOps
**Institution:** [Название учебного заведения]
**GitHub:** https://github.com/f4cax
```

#### Страница "Tasks":
```markdown
# Tasks

This section contains a list of tasks/issues for the project:

1. [Issue #1: ...](https://github.com/f4cax/task-manager/issues/1)
2. [Issue #2: ...](https://github.com/f4cax/task-manager/issues/2)
3. [Issue #3: ...](https://github.com/f4cax/task-manager/issues/3)
4. [Issue #4: ...](https://github.com/f4cax/task-manager/issues/4)

*(Замените на реальные ссылки на ваши issues)*
```

### 3. Добавить логотип (изображение)

Сейчас у вас есть `logo.txt`, но нужно изображение:

1. Создайте простое изображение логотипа (можно использовать онлайн генераторы ASCII art в PNG, или просто создать простой логотип)
2. Сохраните как `logo.png`
3. Добавьте в репозиторий:
```bash
git add logo.png
git commit -m "Add project logo image"
git push origin master
```
4. Обновите README.md - замените `logo.txt` на `logo.png`

### 4. Сделать скриншот Network вкладки - ОБЯЗАТЕЛЬНО!

1. В репозитории на GitHub перейдите на вкладку **Insights** → **Network** (или просто введите в адресной строке: `https://github.com/f4cax/task-manager/network`)
2. Сделайте скриншот всей схемы ветвления (убедитесь, что видна вся структура: master, develop, feature ветки)
3. Сохраните скриншот как `network-diagram.png`
4. Добавьте в репозиторий:
```bash
git add network-diagram.png
git commit -m "Add network branching diagram"
git push origin master
```

### 5. Создать форк - ОБЯЗАТЕЛЬНО!

1. Создайте **НОВЫЙ** репозиторий на GitHub (например, `task-manager-fork`)
2. В локальной папке выполните:
```bash
# Создайте копию вашего проекта
cd ..
git clone https://github.com/f4cax/task-manager.git task-manager-fork
cd task-manager-fork

# Измените remote на новый репозиторий
git remote set-url origin https://github.com/f4cax/task-manager-fork.git

# Загрузите все ветки и теги
git push -u origin master
git push origin develop
git push origin feature/add-task-export
git push --tags
```

### 6. Обновить резюме (для задания на 10/10)

Добавьте в ваше резюме (LinkedIn, GitHub профиль) блок:
```
## Git Flow & GitHub Experience

Successfully completed Git Flow branching workflow project. Confidently use GitHub for version control, issue tracking, and collaborative development.

Project: https://github.com/f4cax/task-manager
```

И добавьте ссылку на резюме в ваш GitHub профиль (Settings → Profile → Website).

## ⚠️ Важные напоминания:

- ✅ При создании Pull Request для feature веток используйте лейбл `feature`
- ✅ При создании Pull Request для hotfix веток используйте лейбл `hotfix`
- ✅ Убедитесь, что все названия веток и коммитов на английском
- ✅ Проверьте, что CHANGELOG.md обновляется при каждом мерже

## 📝 Чек-лист перед сдачей:

- [ ] Labels настроены (feature, hotfix)
- [ ] Wiki создана со всеми разделами (About, What it does, Developer, Tasks)
- [ ] Логотип добавлен (logo.png)
- [ ] Скриншот Network добавлен (network-diagram.png)
- [ ] Форк создан в отдельном репозитории
- [ ] Резюме обновлено (для 10/10)

