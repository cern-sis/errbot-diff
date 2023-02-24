import os

from errbot import BotPlugin, arg_botcmd
from ghapi.all import GhApi


class Errbotdiff(BotPlugin):
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

        files = filter(lambda x: self.is_in_namespace(branch, x), response.files)

        for f in files:
            yield {"file": f}

    @staticmethod
    def is_in_namespace(branch, file):
        return file.filename.split("/")[0] == branch
