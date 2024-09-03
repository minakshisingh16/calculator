#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question - Base Statement Hollister, the Hollister logo and (product name) are trademarks of Hollister Incorported.

Input
Hydrabalance   Yes/No
Hollister Education Yes/No 
Ceraplus  Yes/No

Conditions                     Operations
If Hydrabalance is Yes         Add sentence in the base statement "Hydrabalance and Hydrabalance Logo"
If Hollister Education is Yes  Add sentence in the base statement "Hollister Education" in the Base Statement 
If Ceraplus is Yes             Add sentence in the base statement "Ceraplus" in the Base Statement 
If All Yes                     Add all the sentence in the base statement 

Example Output

Hollister, the Hollister logo, Hydrabalance, Hydrabalance Logo and (product name) are trademarks of Hollister Incorported.
Hollister, the Hollister logo, Hollister Education and (product name) are trademarks of Hollister Incorported.
Hollister, the Hollister logo, Ceraplus and (product name) are trademarks of Hollister Incorported.
Hollister, the Hollister logo,  Hydrabalance and Hydrabalance Logo , Hollister Education ,Ceraplus and (product name) are trademarks of Hollister Incorported.
    


# In[12]:


hydrabalance = input("Is Hydrabalance included (Yes/No)? ")
hollister_education = input("Is Hollister Education included (Yes/No)? ")
ceraplus = input("Is Ceraplus included (Yes/No)? ")
product_name = "Product Name"

def generate_statement(hydrabalance, hollister_education, ceraplus, product_name):
    base_statement = "Hollister, the Hollister logo"
    
    if hydrabalance.lower() == 'yes':
        base_statement += ", Hydrabalance, Hydrabalance Logo"
    if hollister_education.lower() == 'yes':
        base_statement += ", Hollister Education"
    if ceraplus.lower() == 'yes':
        base_statement += ", Ceraplus"
        
    final_statement = f"{base_statement} and ({product_name}) are trademarks of Hollister Incorporated."
    return final_statement

output = generate_statement(hydrabalance, hollister_education, ceraplus, product_name)
print("\nStatement Hollister:")
print(output)


# In[ ]:




