import requests

response = requests.get("https://gitlab.com/api/v4/users/Unnatimishra-14/projects")
my_project = response.json()

for project in my_project:
    print(f"Project name: {project['name']}\n Project Url: {project['web_url']}\n")
