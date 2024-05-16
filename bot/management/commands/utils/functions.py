
from bot.management.commands.services.services import getBasketList
from asgiref.sync import sync_to_async

from foods.models import Food



def captionToCount(caption):
    """
    get product count in: 
        🍟 Food title
        Nx
        N X N So'm = Total N so'm
    """
    try:
        count = int(caption.split('\n')[1].replace("x", ""))
        return count
    
    except:
        count = 1
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    # Radius of the earth in kilometers
    R = 6371.0

    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Differences
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance
    distance = R * c
    return distance

# Test the function
# distance = calculate_distance(48.8566, 2.3522, 51.5074, -0.1278)
# print("Distance (in kilometers):", )

# # Example coordinates (latitude, longitude) in degrees
# lat1 = float(input("Enter the latitude of point 1: "))
# lon1 = float(input("Enter the longitude of point 1: "))
# lat2 = float(input("Enter the latitude of point 2: "))
# lon2 = float(input("Enter the longitude of point 2: "))

# distance = haversine(lat1, lon1, lat2, lon2)
# print("The distance between the two points is {:.2f} kilometers.".format(distance))


def calc_delivered_time(dis, speed):
    # Vaqtni soatlar va minutlarga aylantiramiz
    vaqt_soat = dis / speed

    # Vaqtni soatlar va minutlarga aylantiramiz
    soat = int(vaqt_soat)
    minut = int((vaqt_soat - soat) * 60)

    return f"{soat} soat, {minut} minut" 

async def cleanBaskeAndSetRating(user_id):
    basket = getBasketList(user_id)
    for i in basket:
        food_id = i['food']['id']
        food = await sync_to_async(Food.objects.get)(pk=food_id)
        food.shop_rating += i['count']
        await sync_to_async(food.save)()