# Author: Matt Waggett
# Last updated: 09/17/2012

import sublime, sublime_plugin
import subprocess
import os

class OpenDirectoryOfFileCommand(sublime_plugin.WindowCommand):
	
	def run(self):
		location = sublime.active_window().active_view().file_name()
		if (location != None):
			try:
				if (sublime.platform() == "windows"):
					os.startfile(os.path.dirname(location))
				elif (sublime.platform() == "osx"):
					subprocess.Popen(['open', os.path.dirname(location)])
				else: # linux
					subprocess.Popen(['xdg-open', os.path.dirname(location)])
			except:
				sublime.message_dialog("An error occurred attempting to open the file's folder.")
		else:
			sublime.message_dialog("Cannot find folder for tab. Is this a temporary/unsaved file?")