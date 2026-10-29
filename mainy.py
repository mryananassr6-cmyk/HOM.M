# HOM.M Main Application Entry point 
import finance 
import chat 
import ai_maintenance 

def main():
    print("==========================================")
    print("   welcome to HOM.M PropTech MVP System   ")
    print("==========================================")

    # 1. Testing Finance Module
    print("\n[1] Testing Finance Module:")
    rent_result = finance.check_rent_due("Ahmad Mohamed", 0)
    print(rent_result)

    # 2.Testing Chat Module 
    print("\n[2] Testing Chat Module:")
    chat_response = chat.handle_chat_message("Sara", "I want to ask about maintenance")
    print(chat_response)

    # 3. Testing AI Maintenance Module
    print("\n[3 Testing AI Maintenance Module:")
    maintenance_result = ai_maintenance.classify_maintenance_request("There is an electrical power outage")
    print(maintenance_result)

    print("\n=========================================")
    print("   HOM.M System Initialzed Successfully!   ")
    print("==========================================")

    if __name__ == "__main__":
        main()
# mainy.py - HOM.M Proptech MVP Main Orchestrator 
from finance import calculate_monthly_rent, check_payment_status
from ai_maintenance import classify_maintenance_request
from chat import handle_user_query

def main(): 
    print("=======================================")
    print("    Welcome to HOM.M Protech System    ")
    print("=======================================")
    # 1. Testing Chat Module
    print("\n--- Testing Chat Module ---")
    chat_response = handle_user_query("Hello, I need some help.")
    print(chat_response)
    # 2. Testing Finance Module
    print("\n--- Testing Finance Module ---")
    rent = calculate_monthly_rent(500, 50)
    print(f"Calculated Monthly Rent: ${rent}")
    payment_status = check_payment_status(True)
    print(payment_status)
    # 3. Testing AI Maintenance Module
    print("\n--- Testing AI Maintenance Module ---")
    issue_desc = "there is a severe water leak in the kitchen."
    maintenance_result = classify_maintenance_request(issue_desc)
    print(maintenance_result)
    print("\n=======================================")
    print("     System Executed Successfully      ")
    print("=======================================")
if __name__ == "__main__":
    main()  

        