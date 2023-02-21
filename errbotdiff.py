from errbot import BotPlugin, botcmd
import subprocess
import os

class Errbotdiff(BotPlugin):
    @botcmd
    def diff(self, message, args):
        gh_pat = os.environ["GITHUB_PAT"]
        repo_url = f"https://cern-sis-bot:{gh_pat}@github.com/cern-sis/kubernetes.git"
        remote_branch_1 = "origin/master_output"
        remote_branch_2 = "origin/"+args
        directory=args
        local_path = "kubernetes"

        subprocess.run(["git", "clone", repo_url, local_path])
        subprocess.run(["git", "fetch", "origin"], cwd=local_path)
        cmd = ["git", "diff", f"{remote_branch_1}..{remote_branch_2}", "--", directory]
        result = subprocess.run(cmd, cwd=local_path, capture_output=True, text=True)

        return result.stdout

