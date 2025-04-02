try:
    from unittest import mock
    from unittest.mock import AsyncMock  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    import mock

from google.auth import credentials as ga_credentials

from google.fragment.services.max_results_dataset_service import MaxResultsDatasetServiceClient

from google.fragment.types import test_pagination_max_results_and_wrapper

# =========================================
def test_list_my_dataset_w_max_results_set():
    client = MaxResultsDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = test_pagination_max_results_and_wrapper.ListMaxResultsDatasetRequest(
        max_results=4,
        page_token='page_token_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_max_results_dataset),
            '__call__') as call:

        call.side_effect = (
            test_pagination_max_results_and_wrapper.ListMaxResultsDatasetResponse(
                datasets=[
                    "a",
                    "b",
                    "c",
                    "d",                                        
                    "e",                    
                ],
                next_page_token='abc',   
            ),
            test_pagination_max_results_and_wrapper.ListMaxResultsDatasetResponse(
                datasets=[
                    "f",
                ],
            ),
        )


        pager = client.list_max_results_dataset(request=request)
        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, str)
            for i in results)        
        
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == test_pagination_max_results_and_wrapper.ListMaxResultsDatasetRequest(
            max_results=4,
            page_token='page_token_value',
        )
# =========================================