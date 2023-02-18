#!/usr/bin/env python3.11.1

import subprocess

from datetime import datetime

def get_latest_commit_date(repo_path)->datetime:
    """
        Description:
            Cette fonction récupère la date du dernier commit dans un dépôt git.
        
        Args:
            repo_path (str): Chemin du dépôt git.
        
        Returns:
            datetime: Date du dernier commit.
    """
    git_log = subprocess.run(['git', 'log', '-1', '--pretty=%cI'], cwd=repo_path, capture_output=True, text=True)
    git_log_output = git_log.stdout.strip()
    date = git_log_output.split("+")[0]
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')

def check_code_gitlab_application(date)->str:
    """
        Description:
            Cette fonction vérifie si le code du serveur est à jour.
            
        Args:
            date (datetime): date du dernier commit
            
        Returns:
            str : message de statut de mise à jour
    """
    result = subprocess.run(['git', 'pull'], stdout=subprocess.PIPE)
    if result.stdout == b'Already up to date.\n':
        return f"Le Code déjà à jour ✅ \nDepuis le {date} \nAucun changement à appliquer. 😊 "
    else:
        return f"Le Code est mis à jours ♻️ \nDepuis le {date} \nVeuillez redémarrer l'application pour appliquer les changements. ❗ "


def check_code_gitlab()->dict:
    """
        Description:
            Cette fonction vérifie si le code du serveur est à jour.
        
        Returns:
            bool: True si le code est à jour, False sinon.
    """
    result = subprocess.run(['git', 'pull'], stdout=subprocess.PIPE)
    print(result.stdout)
    if result.stdout == b'Already up to date.\n':
        result_code = {"result_code": "Code déjà à jour"}
    else:
        result_code = {"result_code": "Code mis à jours"}
    
    print(result_code)
    
if __name__ == "__main__":
    check_code_gitlab()
    

