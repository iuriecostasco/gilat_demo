import xml.etree.ElementTree as ET
import re

xml = ET.parse("/home/devasc/labs/devnet-src/gilat_demo/AAC2.xml")
root = xml.getroot()

ns = re.match('{.*}', root.tag).group(0)
body = root.find(f"{ns}Body")
gltag = '{com.gilat.ngnms.server.services.ws.cfg.face}'
creaAAC = body.find(f"{gltag}createApplicationClassification")
AAC = creaAAC.find("applicationClassification")
FWD_IPv4 = AAC.find("fwdLinkIPv4ApplicationClassificationTable")
urn = '{urn:com.gilat.ngnms.server.ws.dto.cfg}FwdLinkIPv4ApplicationClassification'
urn_cont = FWD_IPv4.find(f"{urn}")
stop_ip_source = urn_cont.find("stopSourceIpAddress")
'''
for child in urn_cont:
    print (child.tag)
'''
'''
Tag hierarchy:
<{http://www.w3.org/2003/05/soap-envelope}>
 <{http://www.w3.org/2003/05/soap-envelope}Body>
  <{com.gilat.ngnms.server.services.ws.cfg.face}createApplicationClassification>
   <applicationClassification>
    <fwdLinkIPv4ApplicationClassificationTable>
     <{urn:com.gilat.ngnms.server.ws.dto.cfg}FwdLinkIPv4ApplicationClassification>
      <stopSourceIpAddress>
'''

print("Stop IP source address is: {}".format(stop_ip_source.text))