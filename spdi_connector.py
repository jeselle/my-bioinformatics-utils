import requests

class SPDI_Conector():
    """Collection of helper functions for using SPDI API"""
    
    cosmic_api_url = "https://clinicaltables.nlm.nih.gov/api/cosmic/v4/search"
    spdi_api_url = "https://api.ncbi.nlm.nih.gov/variation/v0/spdi/NC_000001.10%3A12345%3A1%3AA/hgvs"

    def __init__(self):
        pass
        

    def make_api_call(self, http_method, url, params="", headers="", body="", timeout=3):
        try:
            if http_method == 'GET': response = requests.get(url,timeout=timeout)
            elif http_method == 'POST': response = requests.post(url,timeout=timeout)
            else:
                print(f"HTTP method {http_method} not supported")
                System.exit(1)
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
        response.raise_for_status()
        return response.json

def main():
    sc = SPDI_Conector()
    r = sc.make_api_call("GET", sc.spdi_api_url)
    print(r)

if __name__ == "__main__":
    main()