import requests

from config.config import *


def create_project(name):

    headers = {

        "Authorization": f"Bearer {API_TOKEN}",

        "X-Tenant-ID": TENANT

    }

    payload = {

        "name": name,

        "description": "Automation",

        "team_members": []

    }

    return requests.post(

        BASE_URL + "/api/v1/projects",

        headers=headers,

        json=payload

    )