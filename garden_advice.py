# Ask the user for the season and plant type

def get_season_advice(season):
    """Determine advice based on the season"""
    if season == "summer":
        return "Water your plants regularly in a shaded area"
    elif season == "winter":
        return "Protect your plants from extreme cold,snow and wind"
    else:
        return (
            f"Error: '{season}' is not a supported season. "
            "Please choose winter or summer."
            )


def get_plant_advice(plant_type):
    """Determine advice based on the plant type."""
    if plant_type == "flower":
        return "Use fertiliser and a lot of water to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests and winter weather."
    else:
        return (
            f"Error: '{plant_type}' is not a supported plant type. "
            "Please choose flower or vegetable."
        )


def main():
    """Display gardening advice for the user's choices."""
    season = input("Please enter the season: ").strip().lower()
    plant_type = input("Please enter the plant type: ").strip().lower()

    print("\nGardening Advice")
    print("----------------")

    # Check that the season is supported
    if season not in ("summer", "winter"):
        print(get_season_advice(season))
        return

    # Check that the plant type is supported
    if plant_type not in ("flower", "vegetable"):
        print(get_plant_advice(plant_type))
        return

    # Display advice only when both inputs are valid
    print(get_season_advice(season))
    print(get_plant_advice(plant_type))


main()
