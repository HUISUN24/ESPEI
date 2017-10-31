from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

import os
import yaml
from cerberus import Validator

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))

# extension for iseven
class ESPEIValidator(Validator):
    def _validate_iseven(self, iseven, field, value):
        """ Test the oddity of a value.

        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        if iseven and bool(value & 1):
            self._error(field, "Must be an even number")

with open(os.path.join(MODULE_DIR, 'input-schema.yaml')) as f:
    schema = ESPEIValidator(yaml.load(f))

from espei.paramselect import generate_parameters, mcmc_fit
from espei.espei_script import run_espei
