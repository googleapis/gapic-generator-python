# Apply workaround 1 from owlbot.py here https://github.com/googleapis/python-eventarc/blob/main/owlbot.py#L31
# Remove function `parse_service_path`
SED_PATTERN='@staticmethod\n    def parse_service_path'
SED_REPLACE='def parse_service_path'
FILE=tests/integration/goldens/eventarc/google/cloud/eventarc_v1/services/eventarc/client.py
sed -i -z "s/$SED_PATTERN/$SED_REPLACE/g" $FILE
SED_PATTERN_START='def parse_service_path'
SED_PATTERN_END="return m.groupdict()"
FILE=tests/integration/goldens/eventarc/google/cloud/eventarc_v1/services/eventarc/client.py
sed -i "/$SED_PATTERN_START/,/$SED_PATTERN_END/d" $FILE

# Apply workaround 2 from owlbot.py here https://github.com/googleapis/python-eventarc/blob/main/owlbot.py#L39
# Replace `parse_service_path = staticmethod(EventarcClient.parse_service_path)` with ``
SED_PATTERN='parse_service_path = staticmethod(EventarcClient.parse_service_path)'
SED_REPLACE=''
FILE=tests/integration/goldens/eventarc/google/cloud/eventarc_v1/services/eventarc/async_client.py
sed -i "s/$SED_PATTERN/$SED_REPLACE/g" $FILE

# Apply workaround 3 from owlbot.py here https://github.com/googleapis/python-eventarc/blob/main/owlbot.py#L45
# Remove test `test_parse_service_path`
SED_PATTERN_START='def test_parse_service_path'
SED_PATTERN_END="assert expected == actual"
FILE=tests/integration/goldens/eventarc/tests/unit/gapic/eventarc_v1/test_eventarc.py
sed -i "/$SED_PATTERN_START/,/$SED_PATTERN_END/d" $FILE
