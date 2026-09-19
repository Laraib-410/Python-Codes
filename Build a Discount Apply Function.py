#Build A Discount Apply Function:
def apply_discount(price,discount):  #user-defined function
    if not isinstance(price,(int,float)):
        return 'The price should be a number'
    elif  not isinstance (discount,(int,float)):
        return 'The discount should be a number'
    if price<=0:
        return 'The price should be greater than 0'
    if discount<0 or discount>100:
        return 'The discount should be between 0 and 100'
    discount=price*discount/100
    final_price = price - discount
    return final_price
apply_discount(100,20)   #calling a function
apply_discount(200,50)
apply_discount(50,0)
apply_discount(74.5,20.0)