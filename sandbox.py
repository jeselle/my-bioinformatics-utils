
### FUN WITH SPDI API
# from connectors import spdi_connector
# sconn = spdi_connector.SPDI_Conector()
# print(sconn.get_variant_from_hgvs("NC_000007.14:g.55191822_55191823delinsGT"))
# print(sconn.get_hgvs_from_spdi("NC_000001.10:12345:1:A"))

### FUN WITH COSMIC API
from connectors import cosmic_connector
cconn = cosmic_connector.COSMIC_Conector()
print(cconn.get_variant_by_id("COSV56056643"))