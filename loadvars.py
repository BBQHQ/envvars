# import required modules
import os
# pip install python-dotenv
from dotenv import load_dotenv

# load the .env file
load_dotenv()

# load the env vars
def get_env_variable(name):
    """Get the environment variable or return exception"""
    try:
        return os.getenv(name)
    except KeyError:
        error_msg = f"Expected environment variable '{name}' not set."
        raise Exception(error_msg)

# get the env vars from the .env file
var1 = get_env_variable("datavar1")
var2 = get_env_variable("datavar2")

# print the values of the env vars
if __name__ == "__main__":
    print(f'\n{var1}')
    print(f'{var2}\n')