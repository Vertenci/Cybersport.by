from dal.repositories.IndicatorsRepository import IndicatorsRepository


class IndicatorsBLL:
    def __init__(self):
        self.indicators_dal = IndicatorsRepository()

    def fetch_all_indicators(self):
        return self.indicators_dal.get_all()

    def create_indicator(self, form):
        self.indicators_dal.insert(form.save())

    def delete_indicator(self, indicator_id):
        self.indicators_dal.delete(indicator_id)

    def get_indicator(self, indicator_id):
        return self.indicators_dal.get(indicator_id)

    def update_indicator(self, indicator):
        return self.indicators_dal.update(indicator)
