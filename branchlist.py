import requests
import subprocess

def list_all_branches():
    """List all branches in a GitHub repository, including inactive branches."""
    url = f"https://api.github.com/repos/sunlove123/branchtest/git/refs/heads"
    repo_url = "https://github.com/sunlove123/branchtest.git"
    headers = {}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        branches = response.json()
        print("Branches in the repository:")
        result = subprocess.run(['pwd'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        current_directory = result.stdout.strip()
        for branch in branches:
            print(branch['ref'].replace('refs/heads/', ''))
            location = current_directory + "/" + branch['ref'].replace('refs/heads/', '')
            print (location)
            subprocess.run(['mkdir', '-p', location], check=True)
            command = ['git', 'clone', repo_url, '--branch', branch['ref'].replace('refs/heads/', ''), '--single-branch', location]
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result is not None:
                print("Repository successfully cloned.")
            else:
                print("Failed to clone the repository.")


    else:
        print(f"Failed to fetch branches: {response.status_code} {response.reason}")

if __name__ == "__main__":

    list_all_branches()

