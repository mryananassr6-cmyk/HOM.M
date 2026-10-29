def check_rent_due(tenant_name, days_left):
    if days_left == 0:
        return f"URGENT: Today is the rent due date for tenant{tenant_name}!"
    elif days_left < 0:
        return f"WARNING: Rent is overdue for tenant {tenant_name} by {abs(days_left)} days!"
    else:
        return f"Tenant {tenant_name} has {days_left} days remaining until the next rent due date."
    # Testing the function
    if __name__=="__main__":
        print("--- HOM.M Finance Management System ---")
        result = check_rent_due("Ahmed Mohamed", 5)
        print(result)
    # finance.py _ Finance and Rent Management Module 
def calculate_monthly_rent(base_rent, service_fee):
    total = base_rent + service_fee
    return total 
def check_payment_status(is_paid):
 if is_paid:
    return "payment received successfully. Thank you!"
 else:
    return "Warning: Payment is due. Please settle as soon as possible."
 


       

    
                        