import requests

class SPDI_Conector():
    """Collection of helper functions for using SPDI API"""
    
    cosmic_api_url = "https://clinicaltables.nlm.nih.gov/api/cosmic/v4/search"
    spdi_api_url = "https://api.ncbi.nlm.nih.gov/variation/v0"

    def __init__(self):
        pass
    
    def spdi_get_variant_from_hgvs(self, genomic_hgvs):
        response = self.make_api_call("GET", self.spdi_api_url+f"/hgvs/{genomic_hgvs}/contextuals")
        return response.text



    def get_variant_from_hgvs(self, genomic_hgvs):
        response = self.make_api_call("GET", self.spdi_api_url+f"/hgvs/{genomic_hgvs}/contextuals")
        return response.text

    def get_hgvs_from_spdi(self, spdi_string):
        response = self.make_api_call("GET", self.spdi_api_url+f"/spdi/{spdi_string}/hgvs")
        return response.text

    def make_api_call(self, http_method, url, params={}, headers={}, body={}, timeout=3):
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

def main():
    sc = SPDI_Conector()
    r = sc.get_variant_from_hgvs("NC_000007.14:g.55191822_55191823delinsGT")
    print(r)
    r = sc.get_hgvs_from_spdi("NC_000001.10:12345:1:A")
    print(r)

if __name__ == "__main__":
    main()