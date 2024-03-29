from munch import DefaultMunch
import logging
import yaml
from pathlib import Path
def validate_config(config):

    # validate max_level
    for topic in config.topics.keys():
        with open(Path().cwd() / "exercises" / "exercises_general.yaml",'r',encoding='utf8') as file:
                content: dict = DefaultMunch.fromDict(yaml.safe_load(file))
    if config.topics[topic].max_level != 'all':
        if config.topics[topic].max_level > len(content[topic].keys()):

            msg = f"Maximum level  of topic '{topic}' is misspecified. Level suppplied is {config.topics[topic].max_level}. Only levels up to and including {len(content[topic].keys())} are valid."

            logging.exception(msg)
            raise ValueError(msg)

    if type(config.batch_size) != int:
         raise ValueError(f"Batch size must be an integer.")