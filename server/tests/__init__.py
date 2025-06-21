import os

# Path to the environment variables file
env_file_path = "env_vars.txt"

# Load environment variables from the file
if os.path.exists(env_file_path):
    os.environ['DIRECTORY_ENV'] = 'testing'
    with open(env_file_path, "r") as env_file:
        for line in env_file:
            # Strip whitespace and ignore empty lines or comments
            line = line.strip()
            if line and not line.startswith("#"):
                # Split the line into key and value
                key, value = line.split("=", 1)
                os.environ[key] = value.strip()

    print("Environment variables loaded successfully:")
else:
    raise FileNotFoundError(
        f"Error: Environment variables file {env_file_path} not found."
    )
