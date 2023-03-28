#!/usr/bin/env python3.11.1

import subprocess
import os
from datetime import datetime


class Update:
    @staticmethod
    def get_latest_commit_date(repo_path=os.getcwd()) -> datetime:
        """
        Description:
            This function retrieves the date of the latest commit in a git repository.

        Args:
            repo_path (str): Path to the git repository.

        Returns:
            datetime: Date of the latest commit.
        """
        git_log = subprocess.run(
            ["git", "log", "-1", "--pretty=%cI"],
            cwd=repo_path,
            capture_output=True,
            text=True,
        )
        git_log_output = git_log.stdout.strip()
        date = git_log_output.split("+")[0]
        return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")

    @staticmethod
    def check_code_gitlab_application(date=get_latest_commit_date()) -> str:
        """
        Description:
            This function checks if the server code is up to date.

        Args:
            date (datetime): Date of the latest commit.

        Returns:
            str: Update status message.
        """
        try:
            result = subprocess.run(["git", "pull"], stdout=subprocess.PIPE)
            if result.stdout == b"Already up to date.\n":
                return f"The code is already up to date ✅ \nSince {date}\nNo changes to apply. 😊 "
            else:
                return f"The code has been updated ♻️ \nSince {date}\nPlease restart the application to apply the changes. ❗ "
        except Exception as e:
            return f"An error has occurred. ❌ \n{e}"

    @staticmethod
    def check_code_gitlab() -> dict:
        """
        Description:
            This function checks if the server code is up to date.

        Returns:
            dict: Result code of the update status.
        """
        try:
            result = subprocess.run(["git", "pull"], stdout=subprocess.PIPE)
            print(result.stdout)
            if result.stdout == b"Already up to date.\n":
                result_code = {"result_code": "Code already up to date"}
            else:
                result_code = {"result_code": "Code updated"}
            print(result_code)
        except Exception as e:
            result_code = {"result_code": "Error"}
            print(result_code)


if __name__ == "__main__":
    Update.check_code_gitlab()
