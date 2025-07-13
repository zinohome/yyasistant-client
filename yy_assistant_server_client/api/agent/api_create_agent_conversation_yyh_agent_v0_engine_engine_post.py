from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.conversation_id_resp import ConversationIdResp
from ...models.conversation_input import ConversationInput
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    engine: str,
    *,
    body: ConversationInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/yyh/agent/v0/engine/{engine}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ConversationIdResp, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = ConversationIdResp.from_dict(response.json())

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
) -> Response[Union[ConversationIdResp, HTTPValidationError]]:
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
    body: ConversationInput,
) -> Response[Union[ConversationIdResp, HTTPValidationError]]:
    """Create Agent Conversation

     创建agent会话

    Args:
        engine (str):
        body (ConversationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConversationIdResp, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        engine=engine,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    engine: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ConversationInput,
) -> Optional[Union[ConversationIdResp, HTTPValidationError]]:
    """Create Agent Conversation

     创建agent会话

    Args:
        engine (str):
        body (ConversationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConversationIdResp, HTTPValidationError]
    """

    return sync_detailed(
        engine=engine,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    engine: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ConversationInput,
) -> Response[Union[ConversationIdResp, HTTPValidationError]]:
    """Create Agent Conversation

     创建agent会话

    Args:
        engine (str):
        body (ConversationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConversationIdResp, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        engine=engine,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    engine: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ConversationInput,
) -> Optional[Union[ConversationIdResp, HTTPValidationError]]:
    """Create Agent Conversation

     创建agent会话

    Args:
        engine (str):
        body (ConversationInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConversationIdResp, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            engine=engine,
            client=client,
            body=body,
        )
    ).parsed
