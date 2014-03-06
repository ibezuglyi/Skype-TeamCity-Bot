__author__ = 'dit'

from BuildInfo import BuildInfo
import TeamCityRESTApiClient
import json


class TCSkypeClient():

    def __init__(self, tcRestClient=None):
        client = TeamCityRESTApiClient.TeamCityRESTApiClient("admin", "admin", "localhost", 80)
        self.tcRestClient = tcRestClient is None and client or tcRestClient


    def lastBuild(self):
        builds = self.tcRestClient.get_all_builds().get_from_server()
        lastBuild = self._as_builds(builds)[-1]
        return lastBuild

    def _as_builds(self, builds):
        return [BuildInfo(build) for build in builds.values()[1:]]
