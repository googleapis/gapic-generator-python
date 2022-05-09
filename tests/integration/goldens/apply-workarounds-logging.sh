# Apply workaround 1 from owlbot.py here https://github.com/googleapis/python-logging/blob/main/owlbot.py#L26
# Replace attribute `type_` with `type`
SED_PATTERN='monitored_resource_pb2.MonitoredResource(type_'
SED_REPLACE='monitored_resource_pb2.MonitoredResource(type'
FILE=tests/integration/goldens/logging/tests/unit/gapic/logging_v2/test_logging_service_v2.py
sed -i "s/$SED_PATTERN/$SED_REPLACE/g" $FILE
