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
import proto  # type: ignore

from google.cloud.asset_v1.types import assets as gca_assets
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.type import expr_pb2  # type: ignore

__manifest__ = (
        'ExportAssetsResponse',
        'ListAssetsResponse',
        'BatchGetAssetsHistoryResponse',
        'ListFeedsResponse',
        'SearchAllResourcesResponse',
        'SearchAllIamPoliciesResponse',
        'AnalyzeIamPolicyResponse',
        'AnalyzeIamPolicyLongrunningResponse',
)


class ExportAssetsResponse(proto.Message):
    r"""The export asset response. This message is returned by the
    [google.longrunning.Operations.GetOperation][google.longrunning.Operations.GetOperation]
    method in the returned
    [google.longrunning.Operation.response][google.longrunning.Operation.response]
    field.

    Attributes:
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the snapshot was taken.
        output_config (google.cloud.asset_v1.types.OutputConfig):
            Output configuration indicating where the
            results were output to.
        output_result (google.cloud.asset_v1.types.OutputResult):
            Output result indicating where the assets were exported to.
            For example, a set of actual Google Cloud Storage object
            uris where the assets are exported to. The uris can be
            different from what [output_config] has specified, as the
            service will split the output object into multiple ones once
            it exceeds a single Google Cloud Storage object limit.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    read_time = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    output_config = proto.Field(
        proto.MESSAGE,
        number=2,
        message='OutputConfig',
    )
    output_result = proto.Field(
        proto.MESSAGE,
        number=3,
        message='OutputResult',
    )


class ListAssetsResponse(proto.Message):
    r"""ListAssets response.

    Attributes:
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the snapshot was taken.
        assets (Sequence[google.cloud.asset_v1.types.Asset]):
            Assets.
        next_page_token (str):
            Token to retrieve the next page of results.
            It expires 72 hours after the page token for the
            first page is generated. Set to empty if there
            are no remaining results.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    read_time = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    assets = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=gca_assets.Asset,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=3,
    )


class BatchGetAssetsHistoryResponse(proto.Message):
    r"""Batch get assets history response.

    Attributes:
        assets (Sequence[google.cloud.asset_v1.types.TemporalAsset]):
            A list of assets with valid time windows.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    assets = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gca_assets.TemporalAsset,
    )


class ListFeedsResponse(proto.Message):
    r"""

    Attributes:
        feeds (Sequence[google.cloud.asset_v1.types.Feed]):
            A list of feeds.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    feeds = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Feed',
    )


class SearchAllResourcesResponse(proto.Message):
    r"""Search all resources response.

    Attributes:
        results (Sequence[google.cloud.asset_v1.types.ResourceSearchResult]):
            A list of Resources that match the search
            query. It contains the resource standard
            metadata information.
        next_page_token (str):
            If there are more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    results = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gca_assets.ResourceSearchResult,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchAllIamPoliciesResponse(proto.Message):
    r"""Search all IAM policies response.

    Attributes:
        results (Sequence[google.cloud.asset_v1.types.IamPolicySearchResult]):
            A list of IamPolicy that match the search
            query. Related information such as the
            associated resource is returned along with the
            policy.
        next_page_token (str):
            Set if there are more results than those appearing in this
            response; to get the next set of results, call this method
            again, using this value as the ``page_token``.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    @property
    def raw_page(self):
        return self

    results = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gca_assets.IamPolicySearchResult,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class AnalyzeIamPolicyResponse(proto.Message):
    r"""A response message for
    [AssetService.AnalyzeIamPolicy][google.cloud.asset.v1.AssetService.AnalyzeIamPolicy].

    Attributes:
        main_analysis (google.cloud.asset_v1.types.AnalyzeIamPolicyResponse.IamPolicyAnalysis):
            The main analysis that matches the original
            request.
        service_account_impersonation_analysis (Sequence[google.cloud.asset_v1.types.AnalyzeIamPolicyResponse.IamPolicyAnalysis]):
            The service account impersonation analysis if
            [AnalyzeIamPolicyRequest.analyze_service_account_impersonation][]
            is enabled.
        fully_explored (bool):
            Represents whether all entries in the
            [main_analysis][google.cloud.asset.v1.AnalyzeIamPolicyResponse.main_analysis]
            and
            [service_account_impersonation_analysis][google.cloud.asset.v1.AnalyzeIamPolicyResponse.service_account_impersonation_analysis]
            have been fully explored to answer the query in the request.
    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

    class IamPolicyAnalysis(proto.Message):
        r"""An analysis message to group the query and results.

        Attributes:
            analysis_query (google.cloud.asset_v1.types.IamPolicyAnalysisQuery):
                The analysis query.
            analysis_results (Sequence[google.cloud.asset_v1.types.IamPolicyAnalysisResult]):
                A list of
                [IamPolicyAnalysisResult][google.cloud.asset.v1.IamPolicyAnalysisResult]
                that matches the analysis query, or empty if no result is
                found.
            fully_explored (bool):
                Represents whether all entries in the
                [analysis_results][google.cloud.asset.v1.AnalyzeIamPolicyResponse.IamPolicyAnalysis.analysis_results]
                have been fully explored to answer the query.
            non_critical_errors (Sequence[google.cloud.asset_v1.types.IamPolicyAnalysisState]):
                A list of non-critical errors happened during
                the query handling.
        """
        __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore

        analysis_query = proto.Field(
            proto.MESSAGE,
            number=1,
            message='IamPolicyAnalysisQuery',
        )
        analysis_results = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=gca_assets.IamPolicyAnalysisResult,
        )
        fully_explored = proto.Field(
            proto.BOOL,
            number=3,
        )
        non_critical_errors = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=gca_assets.IamPolicyAnalysisState,
        )

    main_analysis = proto.Field(
        proto.MESSAGE,
        number=1,
        message=IamPolicyAnalysis,
    )
    service_account_impersonation_analysis = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=IamPolicyAnalysis,
    )
    fully_explored = proto.Field(
        proto.BOOL,
        number=3,
    )


class AnalyzeIamPolicyLongrunningResponse(proto.Message):
    r"""A response message for
    [AssetService.AnalyzeIamPolicyLongrunning][google.cloud.asset.v1.AssetService.AnalyzeIamPolicyLongrunning].

    """
    __module__ = __module__.rsplit('.', maxsplit=1)[0]  # type: ignore


__all__ = tuple(sorted(__manifest__))
