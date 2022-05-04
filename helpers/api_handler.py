import requests


def make_api_call(http_method, url, params={}, headers={}, body={}, timeout=3):
    try:
        if http_method == 'GET': response = requests.get(url,timeout=timeout)
        elif http_method == 'POST': response = requests.post(url,timeout=timeout)
        else:
            print(f"HTTP method {http_method} not supported")
            System.exit(1)
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting to Resource:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Unspecified Request Error",err)
    response.raise_for_status()
    return response
