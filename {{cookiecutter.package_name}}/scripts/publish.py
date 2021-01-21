import os

import requests
import toml
from requests.models import HTTPError

# [ Read the extension's metadata from pyproject.toml ] --------------------------------------------------------------
# As setup.py will have already run at this stage, we do not need to run the "safety checks" again

pyproject = toml.load(open("pyproject.toml", "r"))
metadata = pyproject.get("imm-extension", {})


base_url = os.environ.get("IMM_STORE_URL")

headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic {}".format(os.environ.get("IMM_STORE_TOKEN")),
}
extension_data = {
    "title": metadata.get("name"),
    "version": metadata.get("version"),
    "url": metadata.get("url"),
    "email": metadata.get("support"),
    "author": metadata.get("vendor"),
    "description": metadata.get("description"),
}

response = requests.post(
    "{}/api/v1/extensions/store/{}/upload".format(base_url, metadata.get("extension")),
    json=extension_data,
    headers=headers,
)
if not response.ok:
    if response.status_code == 401 or response.status_code == 403:
        raise HTTPError("Unauthorised, check IMM_STORE_TOKEN for extension")
    raise HTTPError(f"Got response {response.status_code} from extension store")
