import sublime, sublime_plugin

class AddUnderscoresCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                continue
            selected_text = self.view.substr(region)
            new_selected_text = [
                "_{}_".format(line.strip()) for line in selected_text.split("\n")
            ]
            selected_text = "\n".join(new_selected_text)
            self.view.replace(edit, region, selected_text)
