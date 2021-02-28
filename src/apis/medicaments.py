from flask import Blueprint, request
import json

from src.helpers.api_helper import CustomError, DecimalEncoder
from src.collectors.medicaments_collector import get_medicament

medicaments_api = Blueprint('medicaments_api', __name__)


@medicaments_api.route("/medicaments/sample/<string:count>")
def medicaments_sample_get(count):
    try:
        # result = {'id': 1, 'label': 'test', 'count': count}
        result = get_medicament()
    except:
        return CustomError("GET error, parameters {}".format(count), 400).throw()
    else:
        return json.dumps(result, indent=4, cls=DecimalEncoder)
