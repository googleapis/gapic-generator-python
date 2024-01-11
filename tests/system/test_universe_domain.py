import pytest

# Note(TODO): Uncomment these test cases once showcase library is updated
# def test_universe_domain_validation_pass(echo_with_localhost_universe):
#     assert echo_with_localhost_universe.universe_domain == "localhost:7469"
#     assert echo_with_localhost_universe.api_endpoint == "localhost:7469"
#     response = echo_with_localhost_universe.echo({
#         'content': 'Universe validation succeeded!'
#         })
#     assert response.content == "Universe validation succeeded!"


# def test_universe_domain_validation_fail(echo):
#     assert echo.universe_domain == "localhost:7469"
#     assert echo.api_endpoint == "localhost:7469"
#     with pytest.raises(ValueError) as err:
#         echo.echo({
#             'content': 'Universe validation failed!'
#             })
#     assert err.match("The configured universe domain (localhost:7469) does not match the universe domain found in the credentials (googleapis.com). If you haven't configured the universe domain explicitly, `googleapis.com` is the default.")
