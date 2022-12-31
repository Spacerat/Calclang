from pint import UnitRegistry, Context
import numpy as np

units = UnitRegistry(auto_reduce_dimensions=True)


units.define(
    """
USD = [currency] = dollar = dollars
CAD = nan USD
EUR = nan USD = euros = euro
GBP = nan USD = pounds = pound

@context FX
    EUR = 1.11254 USD
    GBP = 1.16956 EUR
@end
"""
)
