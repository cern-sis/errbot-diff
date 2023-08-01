import os

from errbot import BotPlugin, arg_botcmd
from ghapi.all import GhApi


class Diff(BotPlugin):
    @arg_botcmd(
        "base",
        type=str,
        help="The base branch.",
        template="diff",
    )
    @arg_botcmd(
        "--head",
        type=str,
        help="The head branch.",
        default="master_output",
        template="diff",
    )
    def diff(self, msg, base=None, head=None):
        api = GhApi(
            token=os.environ["GITHUB_PAT"],
            owner="cern-sis",
            repo="kubernetes",
        )

        response = api.repos.compare_commits(
            basehead=f"{base}...{head}",
        )

        files = [f for f in response.files if self.is_in_namespace(base, f)]
        if files:
            return {"files": files}
        else:
            return f":green: **{base}** is up to date."

    @staticmethod
    def is_in_namespace(branch, file):
        return file.filename.split("/")[0] == branch
