from jsonschema.exceptions import ValidationError as ValidationError

def dependencies_draft3(validator, dependencies, instance, schema) -> None: ...
def disallow_draft3(validator, disallow, instance, schema) -> None: ...
def extends_draft3(validator, extends, instance, schema) -> None: ...
def items_draft3_draft4(validator, items, instance, schema) -> None: ...
def minimum_draft3_draft4(validator, minimum, instance, schema) -> None: ...
def maximum_draft3_draft4(validator, maximum, instance, schema) -> None: ...
def properties_draft3(validator, properties, instance, schema) -> None: ...
def type_draft3(validator, types, instance, schema) -> None: ...
