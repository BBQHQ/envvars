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
Clone this repository:
```bash
git clone https://github.com/BBQHQ/envvars.git
```
Navigate to the directory:
```bash
cd envvars
```
The `.env` file is already included in this example repository. It contains the environment variables datavar1 and datavar2. You can modify these values as needed. 

**Note**: If you choose to modify the environemnt variables with sensitive information in your .env file, you should add the .env file to your .gitignore to prevent it from being committed to your repository.

Run the script:
```bash
python loadvars.py
```
The script will print the values of `datavar1` and `datavar2`.
