import subprocess

def check_code(file_path):
    result = subprocess.run(['pylint', file_path, '--disable=all', '--enable=E,W'],
                            stdout=subprocess.PIPE, text=True)
    issues = []
    for line in result.stdout.split('\n'):
        if ':' in line:
            issues.append(line)
    return issues
