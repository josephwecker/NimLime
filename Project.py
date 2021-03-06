import os

import NimLime
import sublime_plugin
from utils.project import get_project_file, set_nim_project

NimLime.add_module(__name__)


class SetProjectCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Retrieve path of project
        st_project = get_project_file(self.window.id())

        if st_project is not None:
            active_view = self.window.active_view()
            filename = active_view.file_name()

            try:
                directory = os.path.dirname(st_project)
                relative_path = os.path.relpath(filename, directory)

                # Set input file
                name, extension = os.path.splitext(relative_path)

                if extension.lower() == ".nim":
                    set_nim_project(st_project, relative_path)

            except:
                raise  # pass
