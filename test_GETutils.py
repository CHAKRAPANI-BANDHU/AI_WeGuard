import re


def getCurlEquivalent(response):
    req = response.request

    command = "curl -v -X {method} '{uri}' -H {headers} -d '{data}'"
    method = req.method
    uri = req.url

    data = req.body.decode('utf-8') if req.body else ''
    data = data.replace("'", "\\'")

    headers = ['"{0}: {1}"'.format(k, v) for k, v in req.headers.items() if
               str(k).startswith("Authorization") or str(k).startswith("Content-Type")]
    headers = " -H ".join(headers)

    return command.format(method=method, headers=headers, data=data, uri=uri)
