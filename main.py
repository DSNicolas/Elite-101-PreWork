retail_name = "Secondary Ikea"

print(f"Hello, this {retail_name}'s chatbot.")
print("I can answer frequently asked questions about the store.")
# Conversation's playout
def conversation():
  question = input("What is your question? \n Questions: \n What are the store's open hours? \n Where is the store located? \n What products are available? \n What are the product's prices? \n Question: ")
  
  if question == "What are the store's open hours?":
    print("\n The store is open from 8 AM - 10 PM on weekdays and 8 AM to 8 PM on weekends. \n")
    respeak = input("Do you have any more questions? ")

  if question == "Where is the store located?":
    print("\n The main store is in Austin, Texas, but there are stores all across America! \n ")
    respeak = input("Do you have any more questions? ")

  if question == "What products are available?":
    print(" \n We sell a variety of home accessories and furniture, ranging from couches and beds to lamps. \n ")
    respeak = input("Do you have any more questions? ")

  if question == "What are the product's prices?":
    print(" \n Prices vary based on what item you are buying")
    print("If you are buying a smaller and simpler item like a lamp, it could range from $20 - $50")
    print("If you are buying a bigger item like a couch, it could range from $500 - $1500. \n ")
    respeak = (input("Do you have any more questions? "))



  if respeak == "yes":
    conversation()
  
  


conversation()