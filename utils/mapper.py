import yaml

# get working dir...


with open('.utils.code_airline.yaml', 'r') as file:
    services = yaml.safe_load(file)

    def find_carrier_name(abbreviation: str) -> str:
        "return the large name or default"
        try: 
            return services[abbreviation]
        except: 
            return abbreviation