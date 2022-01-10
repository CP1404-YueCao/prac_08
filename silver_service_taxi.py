from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Calculate the current fare"""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return a string description of a SilverServiceTaxi"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
