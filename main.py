import requests

original_url = "https://ergast.com/api/f1"

def get_races(original_url, year):
    mod_url = f"{original_url}/{year}.json"
    response = requests.get(mod_url)
    return response.json()

def get_drivers(original_url, year):
    mod_url = f"{original_url}/{year}/drivers.json"
    response = requests.get(mod_url)
    return response.json()

def get_race_results(original_url, year, round):
    mod_url = f"{original_url}/{year}/{round}/results.json"
    response = requests.get(mod_url)
    return response.json()

def quali_results(original_url, year, round):
    mod_url = f"{original_url}/{year}/{round}/qualifying.json"
    response = requests.get(mod_url)
    return response.json()

def current_standings(original_url):
    mod_url = f"{original_url}/current/driverStandings.json"
    response = requests.get(mod_url)
    return response.json()

while True:
 print("""                                                                                                                                                    
#######                                                 #   
#        ####  #####  #    # #    # #        ##        ##   
#       #    # #    # ##  ## #    # #       #  #      # #   
#####   #    # #    # # ## # #    # #      #    #       #   
#       #    # #####  #    # #    # #      ######       #   
#       #    # #   #  #    # #    # #      #    #       #   
#        ####  #    # #    #  ####  ###### #    #     #####
 """)

 print("    Formula 1 Data Reviewer")
 print("=" * 40)
 print("Options:")
 print("1. Get Race Schedule by year")
 print("2. Get Driver List by year")
 print("3. Get Race Results by year and race")
 print("4. Get Quali Results by year and race")
 print("5. Get Current Driver Standings")
 print("6. Exit the program")
 print("=" * 40)
 user_choice = input("Please enter your choice: ")

 if user_choice == "1":
    year = input("Please enter a year:")
    races_list = get_races(original_url, year)
    races = races_list["MRData"]["RaceTable"]["Races"]
    for race in races: 
        print("=============================")
        print(f"Race Name {race['raceName']}")
        print(f"Round {race['round']}")
        print(f"Date {race['date']}")
        print(f"Wiki Link {race['url']}")
        print("=============================")


 elif user_choice == "2":
    year = input("Please enter a year:")
    driver_list = get_drivers(original_url, year)
    drivers = driver_list["MRData"]["DriverTable"]["Drivers"]
    for driver in drivers: 
        print("=============================")
        print(f"Driver First Name: {driver['givenName']}")
        print(f"Driver Last Name: {driver['familyName']}")
        if 'permanentNumber' in driver:
            print(f"Racing Number: {driver['permanentNumber']}")
        else: 
            print("Racing Number: N/A")
        print(f"Nationality: {driver['nationality']}")
        print(f"Date of Birth: {driver['dateOfBirth']}")
        print(f"Wikipedia Page: {driver['url']}")
 elif user_choice == "3":
    year = input("Please enter a year:")
    round_num = input("Please enter which round you want the info for: ")
    results = get_race_results(original_url, year, round_num)
    race_results = results["MRData"]["RaceTable"]["Races"]
    race_num = race_results[0]
    for result in race_results:
        print("=============================")
        print(f"Race Name: {result['raceName']}")
        print(f"Round: {result['round']}")
        print(f"Link for Wikipedia page of race: {result['url']}")
        for result in race_num["Results"]:
            print("=============================")
            print(f"Position: {result['position']}")
            print(f"Driver Name: {result['Driver']['givenName']} {result['Driver']['familyName']}")
            print(f"Constructor (Team): {result['Constructor']['name']}")
            print(f"Constructor Nationality: {result['Constructor']['nationality']}")

 elif user_choice == "4":
    year = input("Please enter a year:")
    round_num = input("Please enter which round you want the quali info for: ")
    quali = quali_results(original_url, year, round_num)
    qualifying_results = quali["MRData"]["RaceTable"]["Races"][0]['QualifyingResults']
    race_info = quali["MRData"]["RaceTable"]["Races"][0]
    print("=============================")
    print(f"Race Name: {race_info['raceName']}")
    print(f"Round: {race_info['round']}")
    print(f"Link for Wikipedia page of race: {race_info['url']}")
    for result in qualifying_results:
        print("=============================")
        print(f"Position: {result['position']}")
        print(f"Name: {result['Driver']['givenName']} {result['Driver']['familyName']}")
        print(f"Constructor: {result['Constructor']['name']}")
        print(f"Q1 Laptime: {result['Q1']}")
        print(f"Q2 Laptime: {result.get('Q2', 'N/A - Did not participate / Didnt set a lap.')}")
        print(f"Q3 Laptime: {result.get('Q3', 'N/A - Did not participate / Didnt set a lap.')}")

 elif user_choice == "5":
    standings_data = current_standings(original_url)
    driver_standings_info = standings_data["MRData"]["StandingsTable"]["StandingsLists"][0]
    driver_standings = standings_data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
    print("=============================")
    print(f"Season: {driver_standings_info['season']}")
    print(f"After Round: {driver_standings_info['round']}")
    for driver in driver_standings:
        print("=============================")
        print(f"Place/Position: {driver['position']}")
        print(f"Name: {driver['Driver']['givenName']} {driver['Driver']['familyName']}")
        print(f"Points: {driver['points']}")
        print(f"Wins this season: {driver['wins']}")
 elif user_choice == "6":
     print("Exiting. Thank you for using my program!")
     break
 else:
     print("Invalid choice.")

 check = input("Do you want to continue or exit? (Y/N): ")
 if check.lower() == "n":
        print("Exiting. Thank you for using my program!")

 elif check.lower() != "y":
        print("Invalid input. Please enter 'Y' to continue or 'N' to exit.")



