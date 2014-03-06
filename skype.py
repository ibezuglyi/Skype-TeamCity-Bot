#!/usr/bin/env python
# -*- coding: utf-8 -*-
from TCSkypeClient import TCSkypeClient

__author__ = 'dit'

import time
import re
import Skype4Py


class SkypeBot(object):
    def __init__(self):
        self.skype = Skype4Py.Skype(Events=self)
        self.skype.FriendlyName = "Team City Skype Bot"
        print self.skype.CurrentUserHandle
        self.skype.Attach()
        self.client = TCSkypeClient()

    def AttachmentStatus(self, status):
        if status == Skype4Py.apiAttachAvailable:
            self.skype.Attach()

    def MessageStatus(self, msg, status):
        if status == Skype4Py.cmsReceived:
            if msg.Chat.Type in (Skype4Py.chatTypeDialog, Skype4Py.chatTypeLegacyDialog):
                for regexp, target in self.commands.items():
                    match = re.match(regexp, msg.Body, re.IGNORECASE)
                    if match:
                        msg.MarkAsSeen()
                        reply = target(self, *match.groups())
                        if reply:
                            msg.Chat.SendMessage(reply)
                            break

    def get_build(self, status):
        return status

    def last_build(self):
        return self.client.lastBuild()

    commands = {
        "build(\d*)": get_build,
        "last_build": last_build
    }


if __name__ == "__main__":
    bot = SkypeBot()

    while True:
        time.sleep(1.0)


