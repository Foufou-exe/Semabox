import subprocess
import os

def get_latest_commit_date(repo_path):
    git_log = subprocess.run(['git', 'log', '-1'], cwd=repo_path, capture_output=True, text=True)
    git_log_output = git_log.stdout
    # Parse the git log output to get the date
    date = git_log_output.split('\n')[2].split(' ')[-6:]
    
    return ' '.join(date)

def check_code_gitlab_application():
    result = subprocess.run(['git', 'pull'], stdout=subprocess.PIPE)
    if result.stdout == b'Already up to date.\n':
        return f"Code déjà à jour ✅ \n Depuis le {datetime.time()}  \n Aucun changement à appliquer. 😊 "
    else:
        return f"Code est mis à jours ♻️ \n Depuis {datetime.time()}  \n Veuillez redémarrer l'application pour appliquer les changements. 😊 "


def check_code_gitlab():
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
    # check_code_gitlab()
    print(get_latest_commit_date(os.getcwd()))

