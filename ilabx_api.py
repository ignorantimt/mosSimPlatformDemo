import hashlib
import json
from typing import Any, Dict, List, TypedDict
import requests
import urllib.parse


class ApiConfig(TypedDict):
    api_base: str
    appid: str
    secret: str


class ErrorResponse(TypedDict):
    code: int
    msg: str


class GetTokenResponse(TypedDict):
    code: int
    access_token: str
    create_time: int
    create_time_display: str
    expires_time: int
    expires_time_display: str
    un: str
    dis: str


class PostDataUploadPayload(TypedDict):
    username: str
    title: str
    childProjectTitle: str
    status: int
    score: int
    startTime: int
    endTime: int
    timeUsed: int
    appid: str
    originId: str
    group_id: str
    group_name: str
    role_in_group: str
    group_members: str
    steps: List["PostDataUploadPayloadStep"]


class PostDataUploadPayloadStep(TypedDict):
    seq: int
    title: str
    startTime: int
    endTime: int
    timeUsed: int
    expectTime: int
    maxScore: int
    score: int
    repeatCount: int
    evaluation: str
    scoringModel: str
    remarks: str
    ext_data: Dict[str, Any]


class PostDataUploadResponse(TypedDict):
    code: int
    id: str


def calculate_signature(ticket: str, api_config: ApiConfig) -> str:
    """Calculate signature for token request.

    Args:
        ticket: Ticket from url.
        appid: Appid from url.

    Returns:
        Signature for token request.
    """

    text = ticket + api_config["appid"] + api_config["secret"]
    hl = hashlib.md5()
    hl.update(text.encode(encoding="utf8"))
    signature = hl.hexdigest().upper()

    return signature


def extract_ticket(url: str) -> str:
    """Extract ticket from url.

    Args:
        url: Url from browser.

    Returns:
        Ticket from url.
    """

    parsed_url = urllib.parse.urlparse(url)

    query_params = urllib.parse.parse_qs(parsed_url.query)

    ticket_params = query_params.get("ticket")

    if ticket_params is None:
        raise ValueError("Ticket not found.")

    if len(ticket_params) != 1:
        raise ValueError("Ticket not found.")

    ticket_raw = ticket_params[0]

    ticket = urllib.parse.unquote(ticket_raw)

    return ticket


def get_token(ticket: str, api_config: ApiConfig) -> GetTokenResponse | ErrorResponse:
    """Get token from server.

    Args:
        ticket: Ticket from url.
        api_config: API config.

    Returns:
        Token information.
    """

    signature = calculate_signature(ticket, api_config)

    url = urllib.parse.urljoin(api_config["api_base"], "token")

    response = requests.get(
        url,
        params={
            "appid": api_config["appid"],
            "ticket": ticket,
            "signature": signature,
        },
    )

    return response.json()


def post_data_upload(
    payload: PostDataUploadPayload, access_token: str, api_base: str
) -> PostDataUploadResponse | ErrorResponse:
    """Post data upload request.

    Args:
        payload: Payload for data upload.
        access_token: Access token from get_token.
        api_base: API base url.

    Returns:
        Response from server.
    """

    url = urllib.parse.urljoin(api_base, "data_upload")

    encoded_payload = json.dumps(payload).encode("utf-8")

    response = requests.post(
        url,
        params={
            "access_token": access_token,
        },
        data=encoded_payload,
    )

    print(payload)

    return response.json()
