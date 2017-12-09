import sublime, sublime_plugin

class SelectWordsCommand(sublime_plugin.TextCommand):

    MIN_WORD_LIMIT = 100
    SECTION_DIVIDER = "#"
	
    def run(self, edit):
        self.view.sel().clear()

		# Remove empty text at beginning
        region = sublime.Region(0, self.view.size())
        if not region.empty():
            doc_text = self.view.substr(region)
            doc_text = doc_text.strip()
            self.view.replace(edit, region, doc_text)


		# Get all text
        region = sublime.Region(0, self.view.size())
        if not region.empty():
            doc_text = self.view.substr(region)
            character_count = 0
            word_count = 0
            for character_count, letter in enumerate(doc_text):
                if letter == self.SECTION_DIVIDER and word_count > self.MIN_WORD_LIMIT:
                    break
                elif letter == " ":
                    word_count += 1

            # Don't try to select more than the entire document
            character_count = min(character_count, self.view.size())

            region = sublime.Region(0, character_count)
            doc_text = self.view.substr(region).strip()
            
            # Select the text
            new_region = sublime.Region(0, len(doc_text))
            self.view.sel().add(new_region)
