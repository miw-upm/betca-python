from http import HTTPStatus
from http.client import responses

print(HTTPStatus.NOT_FOUND.value)
print(HTTPStatus.NOT_FOUND.phrase)

print(responses[404])


