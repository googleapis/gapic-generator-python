# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import Any, AsyncIterator, Awaitable, Callable, Sequence, Tuple, Optional, Iterator

from google.cloud.asset_v1.types import asset_service
from google.cloud.asset_v1.types import assets


class ListAssetsPager:
    """A pager for iterating through ``list_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.ListAssetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``assets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAssets`` requests and continue to iterate
    through the ``assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.ListAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., asset_service.ListAssetsResponse],
            request: asset_service.ListAssetsRequest,
            response: asset_service.ListAssetsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.ListAssetsRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.ListAssetsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = asset_service.ListAssetsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[asset_service.ListAssetsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[assets.Asset]:
        for page in self.pages:
            yield from page.assets

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListAssetsAsyncPager:
    """A pager for iterating through ``list_assets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.ListAssetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``assets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAssets`` requests and continue to iterate
    through the ``assets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.ListAssetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[asset_service.ListAssetsResponse]],
            request: asset_service.ListAssetsRequest,
            response: asset_service.ListAssetsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.ListAssetsRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.ListAssetsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = asset_service.ListAssetsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[asset_service.ListAssetsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[assets.Asset]:
        async def async_generator():
            async for page in self.pages:
                for response in page.assets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class SearchAllResourcesPager:
    """A pager for iterating through ``search_all_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.SearchAllResourcesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchAllResources`` requests and continue to iterate
    through the ``results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.SearchAllResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., asset_service.SearchAllResourcesResponse],
            request: asset_service.SearchAllResourcesRequest,
            response: asset_service.SearchAllResourcesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.SearchAllResourcesRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.SearchAllResourcesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = asset_service.SearchAllResourcesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[asset_service.SearchAllResourcesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[assets.ResourceSearchResult]:
        for page in self.pages:
            yield from page.results

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class SearchAllResourcesAsyncPager:
    """A pager for iterating through ``search_all_resources`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.SearchAllResourcesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchAllResources`` requests and continue to iterate
    through the ``results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.SearchAllResourcesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[asset_service.SearchAllResourcesResponse]],
            request: asset_service.SearchAllResourcesRequest,
            response: asset_service.SearchAllResourcesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.SearchAllResourcesRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.SearchAllResourcesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = asset_service.SearchAllResourcesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[asset_service.SearchAllResourcesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[assets.ResourceSearchResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class SearchAllIamPoliciesPager:
    """A pager for iterating through ``search_all_iam_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.SearchAllIamPoliciesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``results`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchAllIamPolicies`` requests and continue to iterate
    through the ``results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.SearchAllIamPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., asset_service.SearchAllIamPoliciesResponse],
            request: asset_service.SearchAllIamPoliciesRequest,
            response: asset_service.SearchAllIamPoliciesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.SearchAllIamPoliciesRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.SearchAllIamPoliciesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = asset_service.SearchAllIamPoliciesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[asset_service.SearchAllIamPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[assets.IamPolicySearchResult]:
        for page in self.pages:
            yield from page.results

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class SearchAllIamPoliciesAsyncPager:
    """A pager for iterating through ``search_all_iam_policies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.asset_v1.types.SearchAllIamPoliciesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``results`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchAllIamPolicies`` requests and continue to iterate
    through the ``results`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.asset_v1.types.SearchAllIamPoliciesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[asset_service.SearchAllIamPoliciesResponse]],
            request: asset_service.SearchAllIamPoliciesRequest,
            response: asset_service.SearchAllIamPoliciesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.asset_v1.types.SearchAllIamPoliciesRequest):
                The initial request object.
            response (google.cloud.asset_v1.types.SearchAllIamPoliciesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = asset_service.SearchAllIamPoliciesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[asset_service.SearchAllIamPoliciesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[assets.IamPolicySearchResult]:
        async def async_generator():
            async for page in self.pages:
                for response in page.results:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
