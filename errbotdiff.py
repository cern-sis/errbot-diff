from errbot import BotPlugin, arg_botcmd, botcmd
import subprocess


class Errbotdiff(BotPlugin):
    """
    git diff
    """

    def activate(self):
        """
        Triggers on plugin activation

        You should delete it if you're not using it to override any default behaviour
        """
        super(Errbotdiff, self).activate()

    def deactivate(self):
        """
        Triggers on plugin deactivation

        You should delete it if you're not using it to override any default behaviour
        """
        super(Errbotdiff, self).deactivate()

    def get_configuration_template(self):
        """
        Defines the configuration structure this plugin supports

        You should delete it if your plugin doesn't use any configuration like this
        """
        return {
            "EXAMPLE_KEY_1": "Example value",
            "EXAMPLE_KEY_2": ["Example", "Value"],
        }

    def check_configuration(self, configuration):
        """
        Triggers when the configuration is checked, shortly before activation

        Raise a errbot.ValidationException in case of an error

        You should delete it if you're not using it to override any default behaviour
        """
        super(Errbotdiff, self).check_configuration(configuration)

    def callback_connect(self):
        """
        Triggers when bot is connected

        You should delete it if you're not using it to override any default behaviour
        """
        pass

    def callback_message(self, message):
        """
        Triggered for every received message that isn't coming from the bot itself

        You should delete it if you're not using it to override any default behaviour
        """
        pass

    def callback_botmessage(self, message):
        """
        Triggered for every message that comes from the bot itself

        You should delete it if you're not using it to override any default behaviour
        """
        pass

    @botcmd
    def diff(self, message, args):
        # first - clone the repo
        repo_url = "https://github.com/cern-sis/kubernetes.git"
        remote_branch_1 = "origin/master_output"
        remote_branch_2 = "origin/"+args
        directory=args
        local_path = "kubernetes"

        subprocess.run(["git", "clone", repo_url, local_path])
        subprocess.run(["git", "fetch", "origin"], cwd=local_path)
        cmd = ["git", "diff", f"{remote_branch_1}..{remote_branch_2}", "--", directory]
        result = subprocess.run(cmd, cwd=local_path, capture_output=True, text=True)

        return result.stdout

