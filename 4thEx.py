import requests


def test_github_api(username='avielb', min_repositories=5):
    api_url = f'https://api.github.com/users/{username}/repos'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        repositories = response.json()

        if len(repositories) >= min_repositories:
            print(f"Test Passed: At least {min_repositories} repositories found.")
        else:
            print(f"Test Failed: Less than {min_repositories} repositories found.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_github_api()
