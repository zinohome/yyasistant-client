from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.engine_param import EngineParam
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    engine: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/yyh/asr/v0/engine/{engine}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[EngineParam, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = EngineParam.from_dict(response.json())

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
) -> Response[Union[EngineParam, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    engine: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[EngineParam, HTTPValidationError]]:
    """Get ASR Engine param

     获取asr引擎配置参数列表

    Args:
        engine (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EngineParam, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        engine=engine,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    engine: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[EngineParam, HTTPValidationError]]:
    """Get ASR Engine param

     获取asr引擎配置参数列表

    Args:
        engine (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EngineParam, HTTPValidationError]
    """

    return sync_detailed(
        engine=engine,
        client=client,
    ).parsed


async def asyncio_detailed(
    engine: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[EngineParam, HTTPValidationError]]:
    """Get ASR Engine param

     获取asr引擎配置参数列表

    Args:
        engine (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EngineParam, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        engine=engine,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    engine: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[EngineParam, HTTPValidationError]]:
    """Get ASR Engine param

     获取asr引擎配置参数列表

    Args:
        engine (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EngineParam, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            engine=engine,
            client=client,
        )
    ).parsed
