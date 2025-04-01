try:
    from unittest import mock
    from unittest.mock import AsyncMock  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    import mock

from google.auth import credentials as ga_credentials

from google.fragment.services.page_size_dataset_service import PageSizeDatasetServiceClient

from google.fragment.types import test_pagination_page_size

# =========================================
def test_list_my_dataset_w_page_size_set():
    client = PageSizeDatasetServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport='grpc',
    )

    # Populate all string fields in the request which are not UUID4
    # since we want to check that UUID4 are populated automatically
    # if they meet the requirements of AIP 4235.
    request = test_pagination_page_size.ListPageSizeDatasetRequest(
        page_size=4,
        page_token='page_token_value',
    )

    # Mock the actual call within the gRPC stub, and fake the request.
    with mock.patch.object(
            type(client.transport.list_page_size_dataset),
            '__call__') as call:

        call.side_effect = (
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    "a",
                    "b",
                    "c",
                    "d",                                        
                    "e",                    
                ],
                next_page_token='abc',   
            ),
            test_pagination_page_size.ListPageSizeDatasetResponse(
                datasets=[
                    "f",
                ],
            ),
        )


        pager = client.list_page_size_dataset(request=request)
        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, str)
            for i in results)        
        
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        assert args[0] == test_pagination_page_size.ListPageSizeDatasetRequest(
            page_size=4,
            page_token='page_token_value',
        )
# =========================================