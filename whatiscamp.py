__version__ = '0.1.0'
__author__ = 'MsT*|Quick'

import b3
import b3.plugin

class WhatiscampPlugin(b3.plugin.Plugin):

	####################################################################################################################
    ##                                                                                                                ##
    ##   STARTUP                                                                                                      ##
    ##                                                                                                                ##
    ####################################################################################################################

    def onStartup(self):
        """
        Initialize plugin settings.
        """
        self.adminPlugin = self.console.getPlugin('admin')
        if not self.adminPlugin:
            raise AssertionError("could not start without admin plugin")
			
		self._adminPlugin.registerCommand(self, 'whatiscamp', 0, self.cmd_whatiscamp, 'wic')
		
		
	####################################################################################################################
    ##                                                                                                                ##
    ##   Commands                                                                                                     ##
    ##                                                                                                                ##
    ####################################################################################################################
	
	def cmd_whatiscamp(self, data, client, cmd=None):
		"""
		Explain what camp is.
		"""
		if data:
            input = self._adminPlugin.parseUserCmd(data)
        else:
		 client.message('^1I\'m a camper when: ^3I stay more than ^15 seconds ^3at the same spot, hidden or not, and if ^1i\'m not shooting ^3enemies, or if ^1no enemies ^3are shooting me')
		 client.message('^4I\'m not a camper when: ^3I stay more than 5 seconds at the same spot, because ^4i\'m wounded ^3(1hp), because we are ^4medic ^3me, because ^4i\'m fighting^3, because i\'m alone vs ^4more than 2 enemies')