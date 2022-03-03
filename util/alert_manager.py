from .alert import *

class AlertManager:

    alerts = []

    def add_alert(self, category, itemId, itemColor, itemSize, phoneNumber):
        self.alerts.append(Alert(category, itemId, itemColor, itemSize, phoneNumber))

    def check_alerts(self):
        for alert in self.alerts:
            alert.check()
            self.alerts.remove(alert)

    def clear_alerts(self):
        self.alerts.clear()

    def list_alerts(self):
        alerts_str = ''
        for alert in self.alerts:
            alerts_str += alert.to_string() + '\n'
        return alerts_str

