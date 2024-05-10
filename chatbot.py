import random

# Define responses based on rules
responses = {
    "hi": "Hello! Welcome to Pizza Hut. How can I assist you today?",
    "menu": "Sure! Here's our menu:\n1. Pepperoni Pizza\n2. Margherita Pizza\n3. Hawaiian Pizza\n4. Veggie Supreme Pizza\nPlease let me know your choice.",
    "order": "Great choice! Your order has been placed. Please provide your address for delivery.",
    "address": "Thank you! Your order will be delivered to {} shortly. Enjoy your meal!",
    "bye": "Thank you for choosing Pizza Hut. Have a delicious day!",
    "default": "I'm sorry, I didn't quite catch that. Could you please repeat or ask something else?"
}

# Function to generate response based on user input
def generate_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if user input matches any predefined rules
    for key in responses:
        if key in user_input:
            if key == "address":
                return responses[key]
            return responses[key]
    
    # If no rule matches, return a default response
    return responses["default"]

# Main function to handle user interaction
def main():
    print("Welcome to Pizza Hut! How can I assist you today?")
    print("You can start chatting. Type 'bye' to exit.")
    
    ordering = False  # Variable to track if user is in the process of ordering
    address_needed = False  # Variable to track if the address is needed
    
    while True:
        user_input = input("You: ")
        
        # Exit if user inputs 'bye'
        if user_input.lower() == 'bye':
            print("Bot:", generate_response(user_input))
            break
        
        # Generate response based on user input
        response = generate_response(user_input)
        
        # Check if the user is in the process of ordering
        if ordering:
            if address_needed:
                response = generate_response(user_input)  # Response for address provided
                ordering = False  # Reset ordering state
                address_needed = False
            else:
                if "address" in user_input.lower():
                    address_needed = True
                else:
                    response = generate_response("address " + user_input)  # Assume the user input is the address
        
        if "order" in user_input.lower():
            ordering = True  # Set ordering state
        
        print("Bot:", response)

# Run the main function
if __name__ == "__main__":
    main()