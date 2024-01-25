import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json").json()
    # print(response)

    ip = response.get("ip")
    int_prov = response.get("org")
    country = response.get("country")
    region_name = response.get("region")
    city = response.get("city")
    postal = response.get("postal")
    lat = response.get("loc", "").split(",")[0]
    lon = response.get("loc", "").split(",")[1]

    
    if lat is not None and lon is not None:
        
        area = folium.Map(location=[float(lat), float(lon)])
        area.save("Map.html")

    print("[IP] :", ip)
    print("[Int prov] :", int_prov)
    print("[Country] :", country)
    print("[Region name] :", region_name)
    print("[City] :", city)
    print("[ZIP] :", postal)
    print("[Lat] :", lat)
    print("[Lon] :", lon)

def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO BY SNOWFALL'))
    target_ip = input("Please enter a target IP: ")
    get_info_by_ip(ip=target_ip)

if __name__ == "__main__":
    main()