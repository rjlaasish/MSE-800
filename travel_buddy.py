import google.generativeai as genai

genai.configure(api_key=API_KEY)
# example
# genai.configure(api_key='this_is_a_sample_key')

def generate_itinerary(destination, days, interests):
    prompt = f"""
    Create a {days}-day travel itinerary for {destination}.
    The traveler is interested in {', '.join(interests)}.
    Include morning, afternoon, and evening activities for each day.
    Keep it concise and realistic.
    """
    
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("Travel Itinerary Generator\n")
    destination = input("Enter destination: ")
    days = input("Enter number of days: ")
    interests = input("Enter your interests (comma-separated): ").split(",")

    itinerary = generate_itinerary(destination, days, interests)
    print("\nYour Itinerary:\n")
    print(itinerary)
