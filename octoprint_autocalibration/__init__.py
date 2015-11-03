# coding=utf-8
from __future__ import absolute_import


import octoprint.plugin
import octoprint.server

class AutocalibrationPlugin(octoprint.plugin.AssetPlugin,
                            octoprint.plugin.TemplatePlugin):
    def get_assets(self):
        return dict(
            js=["js/autocalibration.js"]
        )

    def get_template_configs(self):
        return [
            dict(type="settings", template="autocalibration_settings.jinja2", custom_bindings=True)
        ]

    def get_update_information(self):
        return dict(
            systemcommandeditor=dict(
                displayName="Autocalibration Plugin",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="platsch",
                repo="OctoPrint-Autocalibration",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/platsch/OctoPrint-Autocalibration/archive/{target_version}.zip"
            )
        )

__plugin_name__ = "Backlash autocalibration"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = AutocalibrationPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }

