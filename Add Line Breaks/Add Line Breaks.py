import sublime, sublime_plugin

class AddLineBreaksCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        region = sublime.Region(0, self.view.size())
        if not region.empty():
            selected_text = self.view.substr(region)
            text_with_linebreaks = selected_text.replace('\n', '\n\n')
            self.view.replace(edit, region, text_with_linebreaks)
