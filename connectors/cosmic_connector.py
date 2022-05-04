from helpers import api_handler

class COSMIC_Conector():
    """Collection of helper functions for using COSMIC API"""
    
    cosmic_api_url = "https://clinicaltables.nlm.nih.gov/api/cosmic/v4/search"

    def __init__(self):
        pass
    
    def search_cosmic_by_term(self, id):
        return api_handler.make_api_call(
            "GET", 
            self.cosmic_api_url, 
            params={"terms": id}).text