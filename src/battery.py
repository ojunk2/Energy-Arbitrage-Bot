class Battery:
    def __init__(self, capacity_kwh=100, max_power_kw=20, efficiency=0.9):
        self.capacity = capacity_kwh  # Total size
        self.max_power = max_power_kw  # Max charge/discharge speed
        self.efficiency = efficiency    # Round-trip losses (heat, etc.)
        self.current_soc = 0.0          # State of Charge (kWh)

    def charge(self, energy_kwh):
        # We can't charge more than the max power or the remaining capacity
        actual_charge = min(energy_kwh * self.efficiency, self.capacity - self.current_soc, self.max_power)
        self.current_soc += actual_charge
        return actual_charge / self.efficiency # Return what we "pulled" from the grid

    def discharge(self, energy_kwh):
        # We can't discharge more than we have or the max power
        actual_discharge = min(energy_kwh, self.current_soc, self.max_power)
        self.current_soc -= actual_discharge
        return actual_discharge * self.efficiency # Return what we "pushed" to the grid