from munch import DefaultMunch
import yaml
from pathlib import Path
def validate_config(config):
    # validate max_level
    for topic in config.topics.keys():
        with open(Path().cwd() / "exercises" / "exercises_general.yaml",'r',encoding='utf8') as file:
                content: dict = DefaultMunch.fromDict(yaml.safe_load(file))
    if config.topics[topic].max_level != 'all':
        if config.topics[topic].max_level > len(content[topic].keys()):
            raise ValueError(f"Topic level is not defined. The entered maximum level for topic '{topic}' is {config.topics[topic].max_level}, but there are only {len(content[topic].keys())} levels available.")
