import sys
import os

from wrappers.ruamel_yaml_wrapper import RuamelYamlWrapper
from ruamel.yaml import YAML
from jinja2 import Template

from typing import Tuple, Iterator, List

from docs_processor import DocsProcessor

script_dir = os.path.dirname(__file__)

r = YAML()

yaml = RuamelYamlWrapper()
data = yaml.load_from_relative_file('examples/azure_devops/azdo_variables_pipeline.yml', script_dir)

processor = DocsProcessor(yaml)

parameters = processor.get_section_docs(data['parameters'])

template_object = open('src/templates/azure_devops/azdo_pipeline_template.jin').read()
template = Template(template_object)
result = template.render(
    _parameters=parameters,
    _file={
        'full_name': 'my_fullName',
        'directory': 'test',
        'name': 'template'
    }
)
print(result)