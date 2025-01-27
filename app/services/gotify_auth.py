from fastapi import Depends
from fastapi.security import APIKeyHeader, APIKeyQuery

app_token_authorization_header = APIKeyHeader(name="Authorization", auto_error=False, description="appTokenAuthorizationHeader (apiKey)")
app_token_header = APIKeyHeader(name="X-Gotify-Key", auto_error=False, description="appTokenHeader (apiKey)")
app_token_query = APIKeyQuery(name="token", auto_error=False, description="appTokenQuery (apiKey)")
basic_auth = APIKeyHeader(name="Authorization", auto_error=False, description="BasicAuth (username:password)")
client_token_authorization_header = APIKeyHeader(name="Authorization", auto_error=False, description="clientTokenAuthorizationHeader (apiKey)")
client_token_header = APIKeyHeader(name="X-Gotify-Key", auto_error=False, description="clientTokenHeader (apiKey)")
client_token_query = APIKeyQuery(name="token", auto_error=False, description="clientTokenQuery (apiKey)")

def gotify_auth(
    app_token_authorization_header: str = Depends(app_token_authorization_header),
    app_token_header: str = Depends(app_token_header),
    app_token_query: str = Depends(app_token_query),
    basic_auth: str = Depends(basic_auth),
    client_token_authorization_header: str = Depends(client_token_authorization_header),
    client_token_header: str = Depends(client_token_header),
    client_token_query: str = Depends(client_token_query),
):
    query, header = "", ""
    if app_token_authorization_header:
        header = app_token_authorization_header
    elif app_token_header:
        header = app_token_header
    elif app_token_query:
        query = app_token_query
    elif basic_auth:
        header = basic_auth
    elif client_token_authorization_header:
        header = client_token_authorization_header
    elif client_token_header:
        header = client_token_header
    elif client_token_query:
        query = client_token_query
    
    query_header: tuple = (query, header)
    return query_header
