import pynetbox
from convert_csv_to_json import get_json_data_dcim, get_key_data
from check_data_netbox import check_regions, netbox

def get_data_site(numerical_order, data):
    region_name=data['region']['{}' .format(numerical_order)]
    region_id= check_regions(region_name)
    add_data = list()
    add_data.append(
        dict (
            name= data['site']['{}' .format(numerical_order)],
            slug= data['site_slug']['{}' .format(numerical_order)],
            region= region_id,
            facility= data['site_facility']['{}' .format(numerical_order)],
        )
    )
    return add_data

def create_sites(key_data, data):
    for numerical_order in key_data:
        add_data = get_data_site(numerical_order, data)
        try:
            netbox.dcim.sites.create(add_data)
        except pynetbox.RequestError as e:
            print(e.error)
    return

def create_site_main():
    data = get_json_data_dcim()
    key_data = get_key_data(data)
    create_sites(key_data, data)
    return