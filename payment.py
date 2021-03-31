class Payment:

    def __init__(self, payment_id, booking_id, deposit_amount):
      self._payment_id = payment_id
      self._booking_id = booking_id
      self._deposit_amount = deposit_amount
    
    @property
    def payment_id(self): 
        return self._payment_id 
      
    @payment_id.setter  
    def payment_id(self, payment_id): 
        self._payment_id = payment_id

    @property
    def booking_id(self): 
        return self._booking_id 
      
    @booking_id.setter
    def set_booking_id(self, booking_id): 
        self._booking_id = booking_id
     
    @property 
    def deposit_amount(self): 
        return self._deposit_amount 

    @deposit_amount.setter  
    def deposit_amount(self, deposit_amount): 
        self._deposit_amount = deposit_amount
