import subprocess


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
    check_code_gitlab()
