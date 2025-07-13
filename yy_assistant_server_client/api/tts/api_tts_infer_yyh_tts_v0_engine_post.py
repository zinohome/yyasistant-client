from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.tts_engine_input import TTSEngineInput
from ...models.tts_engine_output import TTSEngineOutput
from ...types import Response, Unset


def _get_kwargs(
    *,
    body: TTSEngineInput,
    user_id: Union[Unset, str] = "tester",
    request_id: Union[Unset, str] = "",
    cookie: Union[Unset, str] = "",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(user_id, Unset):
        headers["user-id"] = user_id

    if not isinstance(request_id, Unset):
        headers["request-id"] = request_id

    if not isinstance(cookie, Unset):
        headers["cookie"] = cookie

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/yyh/tts/v0/engine",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, TTSEngineOutput]]:
    if response.status_code == 200:
        response_200 = TTSEngineOutput.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, TTSEngineOutput]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TTSEngineInput,
    user_id: Union[Unset, str] = "tester",
    request_id: Union[Unset, str] = "",
    cookie: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, TTSEngineOutput]]:
    """Text To Speech Inference

     执行tts引擎

    Args:
        user_id (Union[Unset, str]): 用户ID Default: 'tester'.
        request_id (Union[Unset, str]): 请求ID Default: ''.
        cookie (Union[Unset, str]): cookie Default: ''.
        body (TTSEngineInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, TTSEngineOutput]]
    """

    kwargs = _get_kwargs(
        body=body,
        user_id=user_id,
        request_id=request_id,
        cookie=cookie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TTSEngineInput,
    user_id: Union[Unset, str] = "tester",
    request_id: Union[Unset, str] = "",
    cookie: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, TTSEngineOutput]]:
    """Text To Speech Inference

     执行tts引擎

    Args:
        user_id (Union[Unset, str]): 用户ID Default: 'tester'.
        request_id (Union[Unset, str]): 请求ID Default: ''.
        cookie (Union[Unset, str]): cookie Default: ''.
        body (TTSEngineInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, TTSEngineOutput]
    """

    return sync_detailed(
        client=client,
        body=body,
        user_id=user_id,
        request_id=request_id,
        cookie=cookie,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TTSEngineInput,
    user_id: Union[Unset, str] = "tester",
    request_id: Union[Unset, str] = "",
    cookie: Union[Unset, str] = "",
) -> Response[Union[HTTPValidationError, TTSEngineOutput]]:
    """Text To Speech Inference

     执行tts引擎

    Args:
        user_id (Union[Unset, str]): 用户ID Default: 'tester'.
        request_id (Union[Unset, str]): 请求ID Default: ''.
        cookie (Union[Unset, str]): cookie Default: ''.
        body (TTSEngineInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, TTSEngineOutput]]
    """

    kwargs = _get_kwargs(
        body=body,
        user_id=user_id,
        request_id=request_id,
        cookie=cookie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TTSEngineInput,
    user_id: Union[Unset, str] = "tester",
    request_id: Union[Unset, str] = "",
    cookie: Union[Unset, str] = "",
) -> Optional[Union[HTTPValidationError, TTSEngineOutput]]:
    """Text To Speech Inference

     执行tts引擎

    Args:
        user_id (Union[Unset, str]): 用户ID Default: 'tester'.
        request_id (Union[Unset, str]): 请求ID Default: ''.
        cookie (Union[Unset, str]): cookie Default: ''.
        body (TTSEngineInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, TTSEngineOutput]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            user_id=user_id,
            request_id=request_id,
            cookie=cookie,
        )
    ).parsed
