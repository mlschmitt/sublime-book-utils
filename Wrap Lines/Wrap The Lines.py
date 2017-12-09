import sublime, sublime_plugin, re

class WrapTheLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        region = sublime.Region(0, self.view.size())
        if not region.empty():
            selected_text = self.view.substr(region)
            text_joined = re.sub(r"(.)\n(.)", r"\1 \2", selected_text)
            self.view.replace(edit, region, text_joined)
