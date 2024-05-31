import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 57
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


@pytest.mark.api
def test_commits_exist(github_api):
    commits = github_api.commits_exist("YaIra1", "PythonAuto")
    assert commits


@pytest.mark.api
def test_commits_count(github_api):
    commits = github_api.get_commits("YaIra1", "PythonAuto")
    commits_count = len(commits)
    assert commits_count > 0
    print(f"Total commits: {commits_count}")


@pytest.mark.api
def test_emoji_exists(github_api):
    emoji = github_api.get_emojis()
    assert "heart" in emoji


@pytest.mark.api
def test_heart_emoji_multiple(github_api):
    emoji = github_api.get_emojis()
    heart_emojis = [url for name, url in emoji.items() if "heart" in name.lower()]
    assert len(heart_emojis) >= 1
    print("Heart emojis found:", heart_emojis)
