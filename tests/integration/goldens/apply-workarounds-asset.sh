# Patch setup.py for asset to install dependencies
SED_INSERT='\        "google-cloud-access-context-manager >= 0.1.2, < 0.2.0dev"'
SED_INSERT+=',\n        "google-cloud-org-policy>=0.1.2, <2.0.0"'
SED_INSERT+=',\n        "google-cloud-os-config >= 1.0.0, <2.0.0dev",'
FILE=tests/integration/goldens/asset/setup.py
sed -i "/grpc\-google/a $SED_INSERT" $FILE

# Apply workaround 1 from owlbot.py here https://github.com/googleapis/python-asset/blob/main/owlbot.py#L28
# Replace `from google.cloud.osconfig.v1 import inventory_pb2` with
# from `google.cloud.osconfig_v1 import Inventory`
SED_PATTERN='from google.cloud.osconfig.v1 import inventory_pb2'
SED_REPLACE='from google.cloud.osconfig_v1 import Inventory'
FILE=tests/integration/goldens/asset/google/cloud/asset_v1/types/assets.py
sed -i "s/$SED_PATTERN/$SED_REPLACE/g" $FILE

# Apply workaround 2 from owlbot.py here https://github.com/googleapis/python-asset/blob/main/owlbot.py#L35
# Replace `inventory_pb2.Inventory` with `Inventory`
SED_PATTERN='inventory_pb2.Inventory'
SED_REPLACE='Inventory'
FILE=tests/integration/goldens/asset/google/cloud/asset_v1/types/assets.py
sed -i "s/$SED_PATTERN/$SED_REPLACE/g" $FILE

# Apply workaround 3 from owlbot.py here https://github.com/googleapis/python-asset/blob/main/owlbot.py#L47
# Remove function `parse_asset_path`
SED_PATTERN='@staticmethod\n    def parse_asset_path'
SED_REPLACE='def parse_asset_path'
FILE=tests/integration/goldens/asset/google/cloud/asset_v1/services/asset_service/client.py
sed -i -z "s/$SED_PATTERN/$SED_REPLACE/g" $FILE
SED_PATTERN_START='def parse_asset_path'
SED_PATTERN_END="return m.groupdict()"
FILE=tests/integration/goldens/asset/google/cloud/asset_v1/services/asset_service/client.py
sed -i "/$SED_PATTERN_START/,/$SED_PATTERN_END/d" $FILE

# Apply workaround 4 from owlbot.py here https://github.com/googleapis/python-asset/blob/main/owlbot.py#L57
# Replace `parse_asset_path = staticmethod(AssetServiceClient.parse_asset_path)` with ``
SED_PATTERN='parse_asset_path = staticmethod(AssetServiceClient.parse_asset_path)'
SED_REPLACE=''
FILE=tests/integration/goldens/asset/google/cloud/asset_v1/services/asset_service/async_client.py
sed -i "s/$SED_PATTERN/$SED_REPLACE/g" $FILE

# Apply workaround 5 from owlbot.py here https://github.com/googleapis/python-asset/blob/main/owlbot.py#L63
# Remove test `test_parse_asset_path`
SED_PATTERN_START='def test_parse_asset_path'
SED_PATTERN_END="assert expected == actual"
FILE=tests/integration/goldens/asset/tests/unit/gapic/asset_v1/test_asset_service.py
sed -i "/$SED_PATTERN_START/,/$SED_PATTERN_END/d" $FILE
