from helpers import api_handler

class SPDI_Conector():
    """Collection of helper functions for using SPDI API"""
    
    cosmic_api_url = "https://clinicaltables.nlm.nih.gov/api/cosmic/v4/search"
    spdi_api_url = "https://api.ncbi.nlm.nih.gov/variation/v0"

    def __init__(self):
        pass
    
    def get_variant_from_hgvs(self, genomic_hgvs):
        response = api_handler.make_api_call("GET", self.spdi_api_url+f"/hgvs/{genomic_hgvs}/contextuals")
        return response.text

    def get_hgvs_from_spdi(self, spdi_string):
        response = api_handler.make_api_call("GET", self.spdi_api_url+f"/spdi/{spdi_string}/hgvs")
        return response.text
