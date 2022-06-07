import os
import requests
# import xmltodict
import json
from common.config import REQUEST_HEADER, PARAMS, PORT, HOST

url = 'https://pycsw-qa-pycsw-route-raster.apps.v0h0bdx6.eastus.aroapp.io/?service=CSW&request=GetRecordById&typenames=mc:MCRasterRecord&ElementSetName=full&resultType=results&outputSchema=http://schema.mapcolonies.com/raster&version=2.0.2&id=3fc674cd-7b77-40ac-8fa3-96b6b4c77f3b'

response = requests.get(url=url, params=PARAMS, headers=REQUEST_HEADER)
# o = xmltodict.parse(response.text)
print(response)
# print(o)
# print(os.environ.get('DOMAIN'))
# print(os.environ.get('ROOT_URL'))
# print(os.environ.get('DEFAULT_HEADERS'))
