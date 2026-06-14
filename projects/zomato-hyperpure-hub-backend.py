def process_hyperpure_hub(raw_truck_id, incoming_manifest):
  new=raw_truck_id.strip()
  if new.startswith("GATEWAY-ENTRY::") and new.endswith("::VERIFIED"):
    vnum=new[21:35]
  else:
    return "ERROR: SECURE GATEWAY BREACH"
  incoming_manifest=set(incoming_manifest)
  incoming_manifest.discard("CRITICAL-TOXIC-PEST")
  incoming_manifest.add("Organic_Certified_Tag")
  incoming_manifest=list(incoming_manifest)
  incoming_manifest.sort()
  clean=incoming_manifest
  top=incoming_manifest[0:2]
  hub_config = (12.9716, 77.5946, "Zone-1")
  try:
    hub_config[2] = "Zone-5"
  except TypeError:
    print("System Lock: Config Integrity Confirmed (Tuples are Immutable)")
  final_payload={
    "vehicle_no": vnum,
    "priority_offload": top,
    "full_clean_manifest": clean,
    "hub_coordinates": hub_config[0:2], # Slice out just the float lat/long values
    "status": "HUB_DISPATCH_READY"}
  return final_payload
truck_log = "   GATEWAY-ENTRY::TRUCK_KA-05-NB-4412::VERIFIED   "

manifest_items = [
    "Fresh_Tomatoes", 
    "Amul_Cream", 
    "Fresh_Tomatoes",  # Duplicate entry!
    "CRITICAL-TOXIC-PEST",  # Contraband item!
    "Ooty_Carrots"
]
hub_dashboard = process_hyperpure_hub(truck_log, manifest_items)
print("\n=================== ZOMATO HYPERPURE HUB DASHBOARD ===================")
import pprint
pprint.pprint(hub_dashboard)
