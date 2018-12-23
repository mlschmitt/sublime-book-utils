import sublime, sublime_plugin

class SelectWordsCommand(sublime_plugin.TextCommand):

    MIN_WORD_LIMIT = 100
    SECTION_DIVIDER = "#"
    
    def run(self, edit):
        self.view.sel().clear()

        # Remove empty text at beginning
        size = self.view.size()
        region = sublime.Region(0, size)
        if not region.empty():
            letters_in = 0
            doc_text = self.view.substr(region)
            for character_count, letter in enumerate(doc_text):
                if letter.strip() == "":
                    letters_in += 1
                    continue
                else:
                    break
            if letters_in > 0:
                region = sublime.Region(0, letters_in)
                self.view.erase(edit, region)
                size = self.view.size()
                region = sublime.Region(0, size)

            # Select text up to next divider
            doc_text = self.view.substr(region)
            character_count = 0
            word_count = 0
            for character_count, letter in enumerate(doc_text):
                if letter == self.SECTION_DIVIDER and word_count > self.MIN_WORD_LIMIT:
                    break
                elif letter == " ":
                    word_count += 1

            # Don't try to select more than the entire document
            character_count = min(character_count, size)

            region = sublime.Region(0, character_count)
            doc_text = self.view.substr(region).strip()
            
            # Select the text
            new_region = sublime.Region(0, len(doc_text))
            self.view.sel().add(new_region)
