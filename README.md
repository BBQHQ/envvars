# Environment Variables Loader

This repository serves as a template for how to interact with environment variables in Python using the `python-dotenv` package. It contains a Python script that loads environment variables from a `.env` file and prints them.

Environment variables are a universal mechanism for conveying configuration information to Unix programs. They can be used to set values that are constant throughout the system, such as the path to the home directory, as well as values that vary from system to system, such as the name of the mail server.

Use cases for environment variables include:

- Storing sensitive information such as API keys, passwords, and database credentials. These values can be stored in the environment to keep them out of your code.
- Configuring software: Many programs look for certain environment variables to set their behavior. For example, a program might look for the `DEBUG` environment variable to determine whether to output debug information.
- Setting the path for software libraries: Some software libraries read environment variables to find the necessary resources. For example, Python uses the `PYTHONPATH` environment variable to determine the list of directories to search for imported modules.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.7+ and pip (Python package installer) installed on your system. The script also requires the `python-dotenv` package. You can install it using pip:

```bash
pip install python-dotenv
```

## Usage
### For Users New to Git:

If you're new to Git, don't worry! Here are two easy ways to get started with this project:

1. **Cloning with Git or GitHub Desktop**:
   - If you prefer using Git on the command line, follow these steps:
     1. Open your terminal.
     2. Run `git clone https://github.com/BBQHQ/envvars` to clone the repository to your local machine.
   - Alternatively, if you prefer a graphical interface, you can use GitHub Desktop:
     1. Download and install [GitHub Desktop](https://desktop.github.com/).
     2. Open GitHub Desktop and click on 'File' > 'Clone Repository'.
     3. Select 'URL' and paste the repository URL, then click 'Clone'.
   These methods will create a local copy of the project on your computer for you to explore and modify.

### For Contributors:

If you'd like to contribute to this project, we encourage you to fork the repository and submit pull requests with your changes. Here's how you can get started:

1. **Forking the Repository**:
   1. Click on the 'Fork' button at the top right corner of this repository's page.
   2. This will create a copy of the repository under your GitHub account.
   3. Make any changes or improvements to your forked copy.
   4. When you're ready, submit a pull request to have your changes reviewed and potentially merged into the main project.

Feel free to choose the method that suits you best, and thank you for your interest in contributing!


The `.env` file is already included in this example repository. It contains the environment variables `datavar1` and `datavar2`. You can modify these values as needed. 

**Note**: If you choose to modify the environemnt variables with sensitive information in your `.env` file, you should add the `.env` file to your `.gitignore` to prevent it from being committed to your repository.

Run the script:
```bash
python loadvars.py
```
The script will print the values of `datavar1` and `datavar2`.

## That's it, you're done!

You did a great job!

Feel free to explore the code and make any modifications as needed...

## Created by BBQHQ

This project was created and is maintained by [BBQHQ](https://github.com/BBQHQ). For any questions or suggestions, please feel free to reach out!
