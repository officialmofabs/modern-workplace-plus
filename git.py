import os
import subprocess

def auto_push(repo_path, commit_message):
    os.chdir(repo_path)
    
    # Add all changes
    subprocess.run(["git", "add", "."])

    # Commit changes
    subprocess.run(["git", "commit", "-m", commit_message])

    # Push changes to the remote repository
    subprocess.run(["git", "push"])

# Path to your local repository
repo_path = "/path/to/your/local/repo"

# Commit message
commit_message = "Auto-push changes"

# Run the auto_push function
auto_push(repo_path, commit_message)
