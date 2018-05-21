from pigg.frame import Model
from pigg.serv import PiggyFly


class XXModel(Model):
    def __init__(self, model):
        super().__init__()
        # load model

    def _pre_process(self, data):
        # pre process data
        return "a"

    def _predict(self, processed_data):
        # use model to predict
        return processed_data


if __name__ == '__main__':
    model = XXModel("")
    PiggyFly(model).serv(8888)