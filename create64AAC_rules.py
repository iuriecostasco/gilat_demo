#Replace all elements from XML file with tag name. E.g. <ca>?</ca> is going to be <ca>${ca}</ca>
import random
VLAN_ID=int("100")
SUBNET_ID=int("1")
for i in range(1,65):
 VLAN_ID=VLAN_ID+1
 SUBNET_ID=SUBNET_ID+1
 operation = random.randrange(1,7)
 print(f"""
      <urn:FwdLinkIPv4ApplicationClassification>
                  <startDestinationIpAddress>0.0.0.0</startDestinationIpAddress>
                  <stopDestinationIpAddress>0.0.0.0</stopDestinationIpAddress>
                  <startDestinationPort>0</startDestinationPort>
                  <stopDestinationPort>65535</stopDestinationPort>
                  <startSourceIpAddress>0.0.0.0</startSourceIpAddress>
                  <stopSourceIpAddress>0.0.0.0</stopSourceIpAddress>
                  <startSourcePort>0</startSourcePort>
                  <stopSourcePort>65535</stopSourcePort>
                  <vlanId>{VLAN_ID}</vlanId>
                  <operation>CS{operation}</operation>
                  <protocol>ANY</protocol>
                  <tosMode>ANY</tosMode>
                  <tosValue>0</tosValue>
               </urn:FwdLinkIPv4ApplicationClassification>
""")
