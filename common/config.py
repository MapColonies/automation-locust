import os
import common.auth

""" CSV """
requests_file = "wmts_csv_user.csv"

# test settings
layer = "2022_04_04T12_01_48Z_MAS_6_ORT_247557-Orthophoto"
gridName = "newGrids"
version = "1.0.0"
projection = "newGrids"
image_format = ".png"
users = 25

runTimeMin = 90
delayBetweenTileRequests = 100  # ms
delayBetweencapabilitiesRequests = 0  # ms

zMin = 0
zMax = 21
""" connection settings """
layer_type = "wmts"
path_builder = f"{layer_type}/{layer}/{projection}/TileMatrix/TileCol/TileRow{image_format}"

HOST = "https://pycsw-qa-pycsw-route-raster.apps.v0h0bdx6.eastus.aroapp.io/"
PORT = 80
REQUEST_HEADER = {'X-API-KEY': os.environ.get('SECRET_VALUE')}
PARAMS = {'service': 'CSW',
          'request': 'GetRecordById',
          'typenames': 'mc:MCRasterRecord',
          'ElementSetName': 'full',
          'resultType': 'results',
          'outputSchema': 'http://schema.mapcolonies.com/raster',
          'version': '2.0.2',
          'id': '3fc674cd-7b77-40ac-8fa3-96b6b4c77f3b'}
