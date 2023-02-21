from errbot import BotPlugin, botcmd
from errbot.templating import tenv
import subprocess
import os

class Errbotdiff(BotPlugin):
    @botcmd(template="diff")
    def diff(self, message, args):
        gh_pat = os.environ["GITHUB_PAT"]
        repo_url = f"https://cern-sis-bot:{gh_pat}@github.com/cern-sis/kubernetes.git"
        remote_branch_1 = "origin/master_output"
        remote_branch_2 = "origin/"+args
        directory=args
        local_path = "kubernetes"

        subprocess.run(["git", "clone", repo_url, local_path])
        subprocess.run(["git", "fetch", "origin"], cwd=local_path)
        cmd = ["git", "diff", "--name-only", f"{remote_branch_1}..{remote_branch_2}", "--", directory]
        result = subprocess.run(cmd, cwd=local_path, capture_output=True, text=True)
        
        changed_files = result.stdout.splitlines()

        for file_path in changed_files:
            cmd = ["git", "diff", f"{remote_branch_1}..{remote_branch_2}", "--", file_path]
            result = subprocess.run(cmd, cwd=local_repo_path, capture_output=True, text=True)
            yield f"Diff for {file_path}: "
            yield tenv().get_template('diff.md').render(diff=result.stdout)

