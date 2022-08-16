from gapic.schema import wrappers

MIXINS_MAP = {
    'DeleteOperation': wrappers.MixinMethod(
        'DeleteOperation',
        request_type = 'operations_pb2.DeleteOperationRequest',
        response_type = 'None'
    ),
    'WaitOperation': wrappers.MixinMethod(
        'WaitOperation',
        request_type = 'operations_pb2.WaitOperationRequest',
        response_type = 'operations_pb2.Operation'
    ),
    'ListOperations': wrappers.MixinMethod(
        'ListOperations',
        request_type = 'operations_pb2.ListOperationsRequest',
        response_type = 'operations_pb2.ListOperationsResponse'
    ),
    'CancelOperation': wrappers.MixinMethod(
        'CancelOperation',
        request_type = 'operations_pb2.CancelOperationRequest',
        response_type = 'None'
    ),
    'GetOperation': wrappers.MixinMethod(
        'GetOperation',
        request_type = 'operations_pb2.GetOperationRequest',
        response_type = 'operations_pb2.Operation'
    ),  
    'TestIamPermissions': wrappers.MixinMethod(
        'TestIamPermissions',
        request_type = 'iam_policy_pb2.TestIamPermissionsRequest',
        response_type = 'iam_policy_pb2.TestIamPermissionsResponse'
    ),
    'GetIamPolicy': wrappers.MixinMethod(     
        'GetIamPolicy',           
        request_type = 'iam_policy_pb2.GetIamPolicyRequest',
        response_type = 'policy_pb2.Policy'
    ),
    'SetIamPolicy': wrappers.MixinMethod(
        'SetIamPolicy',
        request_type = 'iam_policy_pb2.SetIamPolicyRequest',
        response_type = 'policy_pb2.Policy'
    ),
    'ListLocations': wrappers.MixinMethod(
        'ListLocations',
        request_type = 'locations_pb2.ListLocationsRequest',
        response_type = 'locations_pb2.ListLocationsResponse'
    ),
    'GetLocation': wrappers.MixinMethod(
        'GetLocation',
        request_type = 'locations_pb2.GetLocationRequest',
        response_type = 'locations_pb2.Location'
    )
}