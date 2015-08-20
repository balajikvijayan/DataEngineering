import json
import oauth2
import urllib
import urllib2


KEY = "xB81rVIN4OSVI-PEcT0dpg"
SECRET_KEY = "-ybPaAjYbQv9HAMWW-LN63VYmcQ"
TOKEN = "ATlWJsZA957Qg4PTEb6ZFZN7o4HA9D73"
SECRET_TOKEN = "iuQQ1-m_cz4JYszRtMTwfFfBf80"


def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = 'http://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

    consumer = oauth2.Consumer(KEY, SECRET_KEY)
    oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': KEY
        }
    )
    token = oauth2.Token(TOKEN, SECRET_TOKEN)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    print u'Querying {0} ...'.format(signed_url)

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response
