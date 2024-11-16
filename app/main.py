class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
            self.distance_from_city_center = distance_from_city_center
            self.clean_power = clean_power
            self.average_rating = average_rating
            self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> int:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += CarWashStation.calculate_washing_price(self, car)
                CarWashStation.wash_single_car(self, car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car):
        single_car_wash = car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center
        return round(single_car_wash, 1)

    def wash_single_car(self, car: Car):
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        prev = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((prev + rate) / self.count_of_ratings, 1)
