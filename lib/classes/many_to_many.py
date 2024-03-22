class Customer:
    all = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Customer.all.append(self)

        self._reviews = []
        self._restaurants = []

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and 1 < len(first_name) <= 25:
            self._first_name = first_name
        else: 
            print("First name must be a string between 1 and 25 characters")

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and 1 < len(last_name) <= 25:
            self._last_name = last_name
        else: 
            print("Last name must be a string between 1 and 25 characters")

    def reviews(self):
        return [review for review in Review.all if review.customer == self]
        
    def restaurants(self):
        return list(set(review.restaurants for review in self._reviews))

    def num_negative_reviews(self):
        negative_reviews = 0

        for review in self.reviews():
            if review.rating in [1,2]:
                negative_reviews += 1
        return negative_reviews

    def has_reviewed_restaurant(self, restaurant):
        for review in self.reviews():
            if review.restaurant == restaurant:
                return True
            else:
                return False         
    
class Restaurant:
    all = []

    def __init__(self, name):
        self.name = name
        Restaurant.all.append(self)

        self._reviews = []
        self._customers = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 1:
            self._name = name
        else: 
            print("Name must be a string greater than or equal to 1 characters")

    def reviews(self):
        return [review for review in Review.all if review.restaurant == self]

    def customers(self):
        return list(set(review.customer for review in self._reviews))

    def average_star_rating(self):
        return round(sum([review.rating for review in Review.all if review.restaurant == self]) / len([review.rating for review in Review.all if review.restaurant == self]), 1) if len([review.rating for review in Review.all if review.restaurant == self]) > 0 else 0.0

    @classmethod
    def top_two_restaurants(cls):
        restaurant_with_avg_rating = {}
        for restaurant in cls.all:
            avg_rating = round(sum([review.rating for review in Review.all if review.restaurant == restaurant]) / len([review.rating for review in Review.all if review.restaurant == restaurant]), 1) if len([review.rating for review in Review.all if review.restaurant == restaurant]) > 0 else 0.0
            restaurant_with_avg_rating[restaurant] = avg_rating
        sorted_restaurant_with_avg_rating = dict(sorted(restaurant_with_avg_rating.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_restaurant_with_avg_rating.keys())[:2] if len(Review.all) > 0 else None
    
class Review:
    all = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all.append(self)

        customer._restaurants.append(self)
        customer._reviews.append(customer)

        restaurant._reviews.append(self)
        restaurant._customers.append(restaurant)

    @property
    def customer (self):
        return self._customer

    @property 
    def restaurant (self):
        return self._restaurant

    @property
    def rating (self):
        return self._rating

    @customer.setter
    def customer (self, customer): 
        if isinstance (customer, Customer):
            self._customer = customer
        else:
            print("Customer must be an instance of Customer")

    @restaurant.setter
    def restaurant (self, restaurant): 
        if isinstance (restaurant, Restaurant):
            self._restaurant = restaurant
        else:
            print("Customer must be an instance of Customer")

    @rating.setter
    def rating(self, rating):
        if type(rating) is int and 1 <= rating <= 5 and not hasattr(self, "rating"):
            self._rating = rating
        else:
            print("Rating must be an integer from 1-5 and cannot be changed")

