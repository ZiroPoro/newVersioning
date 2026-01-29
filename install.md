# Installation Guide

This guide will help you install and set up the Task Manager application on your system.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/username/task-manager.git
cd task-manager
```

### 2. Verify Python Installation

Check if Python is installed on your system:

```bash
python --version
```

or

```bash
python3 --version
```

You should see Python 3.7 or higher.

### 3. Install Dependencies

This project currently has no external dependencies. However, if you want to set up a virtual environment (recommended):

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

### 4. Run the Application

Execute the application:

```bash
python app.py
```

## Usage

Once the application is running, you can use the following commands:

- `add` - Add a new task
- `list` - Display all tasks
- `complete` - Mark a task as completed (requires task ID)
- `remove` - Remove a task (requires task ID)
- `exit` - Exit the application

## Troubleshooting

### Python not found

If you get a "Python not found" error:
- Make sure Python is installed and added to your system PATH
- Try using `python3` instead of `python`

### Permission errors

If you encounter permission errors:
- On Linux/Mac, you may need to use `sudo` (not recommended)
- On Windows, run the terminal as Administrator if needed

## Uninstallation

To remove the application:

1. Delete the project directory
2. If you created a virtual environment, you can simply delete the `venv` folder

## Support

For issues or questions, please open an issue in the GitHub repository.

