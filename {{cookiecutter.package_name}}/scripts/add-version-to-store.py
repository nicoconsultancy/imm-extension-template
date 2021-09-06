import os
import sys

import requests  # noqa: E402
import toml  # noqa: E402
from requests.models import HTTPError  # noqa: E402

# [ Read the extension's metadata from pyproject.toml ] --------------------------------------------------------------
# As setup.py will have already run at this stage, we do not need to run the "safety checks" again

pyproject = toml.load(open("pyproject.toml"))
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
sys.stdout.write(f"About to upload to {base_url} with extension {extension_data}")
response = requests.post(
    "{}/api/v1/extensions/store/{}/upload".format(base_url, metadata.get("extension")),
    json=extension_data,
    headers=headers,
)
if not response.ok:
    if response.status_code == 401 or response.status_code == 403:
        raise HTTPError("Unauthorised, check IMM_STORE_TOKEN for extension")
    elif response.status_code == 400:
        raise HTTPError(f"Badly formatted request: {response.json()}")
    raise HTTPError(f"Got response {response.status_code} from extension store")
