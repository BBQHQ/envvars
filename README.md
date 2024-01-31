# Environment Variables Loader

This repository contains a Python script that loads environment variables from a `.env` file and prints them.

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
Create a `.env` file in the root directory and add your environment variables:
```bash
echo "datavar1=yourvalue1" >> .env
echo "datavar2=yourvalue2" >> .env
```
Run the script:
```bash
python loadvars.py
```
The script will print the values of `datavar1` and `datavar2`.
