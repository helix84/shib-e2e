from configparser import ConfigParser
import requests
import json
from types import SimpleNamespace
import os

configPath = os.path.join(os.path.dirname(__file__), '../config.ini')


class User:
    def __init__(self):
        user = self.parse_user_from_config();
        self.Name = user[0]
        self.Password = user[1]

    def get_name(self):
        return self.Name

    def get_password(self):
        return self.Password

    @staticmethod
    def parse_user_from_config():
        config_object = ConfigParser()
        config_object.read(configPath)

        userinfo = config_object["USER"]
        return userinfo["name"], userinfo["password"]


class ESource:
    def __init__(self, source_id, facet_access, title_display, link_native_home, wayfless, link_publisher, active):
        self.source_id = source_id
        self.facet_access = facet_access
        self.title_display = title_display
        self.link_native_home = link_native_home
        self.wayfless = wayfless
        self.link_publisher = link_publisher
        self.active = active


class Data:
    def __init__(self):
        self.e_source_list = None
        self.json_response = None
        self.user = None
        self.proxy_url = None
        self.is_vpn_enabled = None
        self.get_user()
        self.get_json_e_resources()
        self.get_e_source_list()
        self.parse_proxy_from_config()
        self.parse_vpn_from_config()

    def parse_proxy_from_config(self):
        config_object = ConfigParser()
        config_object.read(configPath)

        proxy = config_object["PROXY"]
        self.proxy_url = proxy["proxy_url"]

    def parse_vpn_from_config(self):
        config_object = ConfigParser()
        config_object.read(configPath)

        vpn = config_object["VPN"]
        self.is_vpn_enabled = vpn["isEnabled"]

    def get_user(self):
        self.user = User()

    def get_json_e_resources(self):
        try:
            response = requests.get("https://www-new.k.utb.cz/eresources-list.php")
            response.raise_for_status()
            self.json_response = response
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

    def get_e_source_list(self):
        e_source_list = []
        if self.json_response:
            json_source = json.loads(self.json_response.text, object_hook=lambda d: SimpleNamespace(**d))
            for e_source in json_source:
                e_source_list.append(ESource(e_source.source_id, e_source.facet_access, e_source.title_display,
                                             e_source.link_native_home, e_source.wayfless, e_source.link_publisher,
                                             e_source.active))
            self.e_source_list = e_source_list
        else:
            raise print("Error by parsing json to ESource")
