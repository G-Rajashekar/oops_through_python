class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price 
        self.rating=rating
        self.you_saved=price-deal_price
    
    def display_product_details(self):
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price)) 
        print("Deal_Price: {}".format(self.deal_price)) 
        print("Rating: {}".format(self.rating))
        print("You Saved: {}".format(self.you_saved))  
    
    def get_deal_price(self):
        return self.deal_price 
    

class ElectronicItem(Product):
    def __init__(self,name,price,deal_price,rating,warranty_in_months):
        super().__init__(name,price,deal_price,rating)
        self.warranty_in_months=warranty_in_months 
    
    def display_product_details(self):
        super().display_product_details()
        print("Warranty_in_months: {}".format(self.warranty_in_months))
    

class GroceryItem(Product):
    def __init__(self,name,price,deal_price,rating,expiry_date):
        super().__init__(name,price,deal_price,rating)
        self.expiry_date=expiry_date 
    
    def display_product_details(self):
        super().display_product_details()
        print("Expiry Date: {}".format(self.expiry_date))  

class Order:
     delivery_charges={
         "Normal":0,
         "Prime":50
     }
     def __init__(self,delivery_method,delivery_address):
         self.items_in_cart=[]
         self.delivery_method=delivery_method 
         self.delivery_address=delivery_address 
    
     def add_items_in_cart(self,product,quantity):
        self.items_in_cart.append((product,quantity)) 
    
     def display_cart_items(self):
         print("Delivery Method: {}".format(self.delivery_method))
         print("Delivery Address: {}".format(self.delivery_address)) 
         for product,quantity in self.items_in_cart:
             product.display_product_details()
             print("Quantity: {}".format(quantity)) 
             print("") 
         print("-------------------------------") 
         total_bill=self.get_total_bill() 
         print("Total Bill: {}".format(total_bill)) 
    
     def get_total_bill(self):
        total_bill=0
        for product,quantity in self.items_in_cart:
            deal_price=product.get_deal_price() 
            total_bill+=(quantity*deal_price) 
        order_charges=self.delivery_charges[self.delivery_method] 
        total_bill+=order_charges 
        return total_bill 

     def update_delivery_charges(cls,delivery_method,charges):
         cls.delivery_charges[delivery_method]=charges 

obj=ElectronicItem("iphone",50000,40000,4.3,12)
order_obj=Order("Normal",4-16)
order_obj.add_items_in_cart(obj,2)
order_obj.display_cart_items() 