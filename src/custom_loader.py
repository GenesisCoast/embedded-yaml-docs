from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

class Hero:
    yaml_tag = '!Hero'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def to_yaml(cls, representer, data):
        return representer.represent_mapping(cls.yaml_tag,
                                             {'name': data.name, 'age': data.age})

    @classmethod
    def from_yaml(cls, constructor, node):
        data = CommentedMap()
        constructor.construct_mapping(node, data, deep=True)
        print(data)
        return cls(**data)

    def __str__(self):
        return "Hero(name -> {}, age -> {})".format(self.name, self.age)
