# Инструкция по созданию форка

## Что такое форк в контексте этого задания?

**Форк** - это создание **отдельного нового репозитория**, который является копией вашего основного репозитория. Это нужно для демонстрации, что вы умеете работать с несколькими репозиториями.

## Пошаговая инструкция:

### Шаг 1: Создайте новый репозиторий на GitHub

1. Перейдите на https://github.com
2. Нажмите кнопку **"New repository"** (или плюсик справа вверху → New repository)
3. Назовите репозиторий, например: `task-manager-fork` или `task-manager-copy`
4. **ВАЖНО**: 
   - Сделайте его **Public**
   - **НЕ** добавляйте README, .gitignore или лицензию
   - Просто создайте пустой репозиторий

### Шаг 2: Скопируйте ваш проект в новую папку

Откройте терминал (PowerShell) и выполните:

```bash
# Перейдите на уровень выше вашей текущей папки
cd ..

# Склонируйте ваш основной репозиторий в новую папку
git clone https://github.com/f4cax/task-manager.git task-manager-fork

# Перейдите в новую папку
cd task-manager-fork
```

### Шаг 3: Измените remote на новый репозиторий

```bash
# Удалите старый remote
git remote remove origin

# Добавьте новый remote (замените f4cax на ваш username, если другой)
git remote add origin https://github.com/f4cax/task-manager-fork.git

# Проверьте, что remote правильный
git remote -v
```

### Шаг 4: Загрузите все ветки и теги в новый репозиторий

```bash
# Загрузите master ветку
git push -u origin master

# Загрузите develop ветку
git push origin develop

# Загрузите feature ветку (если она еще не смержена)
git push origin feature/add-task-export

# Загрузите все теги
git push --tags
```

### Готово! 

Теперь у вас есть два репозитория:
- `task-manager` - основной
- `task-manager-fork` - форк (копия)

## Проверка:

Откройте в браузере: `https://github.com/f4cax/task-manager-fork` - там должны быть все ваши файлы, ветки и теги.

---

## Про резюме (для задания на 10/10)

**Резюме** - это ваше личное резюме (CV), которое вы используете для поиска работы.

### Что нужно сделать:

1. **Добавить в резюме блок о Git Flow:**
   
   Откройте ваше резюме (LinkedIn, личный сайт, или файл резюме) и добавьте раздел, например:

   ```
   ## Technical Skills / Projects
   
   **Git Flow & GitHub Experience**
   Successfully completed Git Flow branching workflow project. 
   Confidently use GitHub for version control, issue tracking, 
   and collaborative development.
   
   Project: https://github.com/f4cax/task-manager
   ```

2. **Добавить ссылку на резюме в GitHub профиль:**
   
   - Перейдите на https://github.com/settings/profile
   - В поле **"Website"** или **"Bio"** добавьте ссылку на ваше резюме
   - Например: `https://linkedin.com/in/ваш-профиль` или `https://ваш-сайт.com/resume`

### Это обязательно?

- **Для 5/10 и 7/10** - НЕТ, это не обязательно
- **Для 10/10** - ДА, это обязательное требование

Если вы не хотите делать резюме, можете просто пропустить этот пункт, но тогда максимальная оценка будет 7/10.

