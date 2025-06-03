capital = {"Indonesia":"Jakarta",
           "Malaysia": "Kuala Lumpur",
           "French": "Paris"
           }
travel_log = {"Indonesia": ["jakarta", "bandung", "Bogor"]
              }

nested_list = ["A", "B", ["C", "D"]]

travel_log2 = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Indonesia"][2])
print(nested_list[2][1])
print(travel_log2["Germany"]["cities_visited"][2])
