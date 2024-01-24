import streamlit as st

class MetroAssistantChatbot:
    def __init__(self):
        self.metro_schedule = {
            "weekdays": {"start": "5:30am", "end": "11:00pm"},
            "weekends": {"start": "5:30am", "end": "12:00am"}
        }
        self.metro_stations = {
            "Purple": ["Urban Crossroads Station", "Civic Circle Junction"],
            "Green": ["Skylight Square Junction", "Downtown Gateway"],
            "Junction/Intersection": ["Cityscape Central"]
        }
        self.metro_prices = {
            ("Cityscape Central", "Urban Crossroads Station"): 14.25,
            ("Urban Crossroads Station","Cityscape Central"): 14.25,
            ("Cityscape Central", "Civic Circle Junction"): 13.0,
            ("Civic Circle Junction","Cityscape Central"): 13.0,
            ("Cityscape Central", "Skylight Square Junction"): 12.50,
            ("Skylight Square Junction","Cityscape Central"): 12.50,
            ("Cityscape Central", "Downtown Gateway"): 18.55,
            ("Downtown Gateway","Cityscape Central"): 18.55,
            ("Urban Crossroads Station", "Civic Circle Junction"): 20,
            ("Civic Circle Junction","Urban Crossroads Station"): 20,
            ("Urban Crossroads Station", "Skylight Square Junction"): 23.05,
            ("Skylight Square Junction","Urban Crossroads Station"): 23.05,
            ("Urban Crossroads Station", "Downtown Gateway"): 24.50,
            ("Downtown Gateway","Urban Crossroads Station"): 24.50,
            ("Civic Circle Junction", "Skylight Square Junction"): 28.88,
            ("Skylight Square Junction","Civic Circle Junction"): 28.88,
            ("Civic Circle Junction", "Downtown Gateway"): 27.65,
            ("Downtown Gateway","Civic Circle Junction"): 27.65,
            ("Skylight Square Junction", "Downtown Gateway"): 25.05,
            ("Downtown Gateway","Skylight Square Junction"): 25.05,
        }
        self.emergency_number = "1800-425-12345"
        self.support_email = "travelhelp@bmrc.co.in"

    def get_schedule(self, day_type):
        return self.metro_schedule[day_type]

    def get_stations_on_lane(self, lane):
        return self.metro_stations.get(lane, [])

    def get_price(self, source_station, destination_station):
        key = (source_station, destination_station)
        return self.metro_prices.get(key, None)

    def get_emergency_number(self):
        return self.emergency_number

    def get_support_email(self):
        return self.support_email

    def get_travel_info(self, source_station, destination_station):
        if source_station == destination_station:
            return f"You are already at {source_station}. No travel needed."

        if source_station in self.metro_stations["Junction/Intersection"] or \
                destination_station in self.metro_stations["Junction/Intersection"]:
            return f"Direct connectivity from {source_station} to {destination_station}. No transfers needed."

        return f"Travel from {source_station} to {destination_station} requires a transfer at Cityscape Central Station."

    def cancel_ticket(self):
        return "Sorry, tickets once booked cannot be canceled."

    def get_refund_info(self):
        return "I’m sorry, I cannot help you with this. Please check at the counter or call the Emergency number: " \
               f"{self.emergency_number}, or mail us at {self.support_email}."

# Function to process user input and return bot response
def process_user_input(user_input, metro_bot):
    user_input_lower = user_input.lower()
    if not user_input:
        return "Welcome to Metro! How can I assist you today?"
    if any(greeting in user_input_lower for greeting in ["hi", "hello", "hey"]):
        return "Hello there! How can I assist you today?"
    if "schedule" in user_input_lower:
        day_type = st.text_input("Which day are you interested in? (weekdays/weekends): ")
        schedule = metro_bot.get_schedule(day_type)
        return f"The metro operates from {schedule['start']} to {schedule['end']} on {day_type}."
    if "what is metro" in user_input_lower:
        return "Metro is a rapid transit system or railway system typically serving a city and its suburbs with high-capacity public transportation."

    elif "stations" in user_input_lower:
        lane = st.text_input("Which lane are you interested in? (Purple/Green): ")
        stations = metro_bot.get_stations_on_lane(lane)
        return f"The stations on the {lane} lane are: {', '.join(stations)}."

    elif "price" in user_input_lower:
        source_station = st.text_input("Enter the source station: ")
        destination_station = st.text_input("Enter the destination station: ")
        price = metro_bot.get_price(source_station, destination_station)
        if price is not None:
            return f"The price from {source_station} to {destination_station} is {price}."
        else:
            return f"Could not find the price for the specified journey."

    elif "emergency" in user_input_lower:
        emergency_number = metro_bot.get_emergency_number()
        return f"In case of emergency, call {emergency_number}."

    elif "email" in user_input_lower or "support" in user_input_lower:
        support_email = metro_bot.get_support_email()
        return f"For support, you can email us at {support_email}."

    elif "travel" in user_input_lower:
        source_station = st.text_input("Enter the source station: ")
        destination_station = st.text_input("Enter the destination station: ")
        travel_info = metro_bot.get_travel_info(source_station, destination_station)
        return travel_info

    elif "cancel" in user_input_lower:
        return metro_bot.cancel_ticket()

    elif "refund" in user_input_lower:
        return metro_bot.get_refund_info()

    else:
        return "I'm sorry, I didn't understand that. Please ask another question or type 'exit' to end the chat."

# Streamlit App
def main():
    st.title("Metro Assistance Chatbot")

    st.sidebar.header("Chatbot")
    user_input = st.sidebar.text_input("You:", "")

    metro_bot = MetroAssistantChatbot()
    response = process_user_input(user_input, metro_bot)

    st.sidebar.text_area("Metro Assistance Chatbot:", response)

if __name__ == "__main__":
    main()
