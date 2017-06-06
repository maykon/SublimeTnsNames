import sublime, sublime_plugin

class OpenTnsnamesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = sublime.load_settings('SublimeTnsNames.sublime-settings')
		self.view.window().open_file(settings.get(sublime.platform()+'_tnsnames_file_location'))

