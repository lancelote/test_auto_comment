import argparse
import os

from github import Github

DOC_LABEL = "to be documented"
DOC_MSG = "Hello @lancelote"


def env(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise Exception(f"{key} is not set")
    return value


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", type=str, required=True)
    parser.add_argument("--pull_request", type=int, required=True)
    args = parser.parse_args()

    repo = env("GITHUB_REPOSITORY")

    g = Github(args.token)
    repo = g.get_repo(repo)
    pr = repo.get_pull(args.pull_request)

    pr.create_issue_comment(DOC_MSG)
