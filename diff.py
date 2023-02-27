import os

from errbot import BotPlugin, arg_botcmd
from ghapi.all import GhApi


class Diff(BotPlugin):
    @arg_botcmd(
        "branch",
        help="The branch to diff.",
        template="diff",
    )
    def diff(self, msg, branch=None):
        api = GhApi(
            token=os.environ["GITHUB_PAT"],
            owner="cern-sis",
            repo="kubernetes",
        )

        response = api.repos.compare_commits(
            basehead=f"{branch}...master_output",
        )

        files = [f for f in response.files if self.is_in_namespace(branch, f)]
        if files:
            return {"files": files}
        else:
            return f":green: **{branch}** is up to date."

    @staticmethod
    def is_in_namespace(branch, file):
        return file.filename.split("/")[0] == branch
