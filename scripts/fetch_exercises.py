from munch import DefaultMunch
from numpy import array
from numpy.random import choice
from pathlib import Path
import logging
import yaml


from scripts.candidate_levels_per_topic import candidate_levels_per_topic
from scripts.instantiate_exercise import instantiate_exercise

def fetch_exercises(config: dict):

    # get templates of exercises. structure: topic - level
    with open(Path().cwd() / "exercises" / "exercises_general.yaml",'r',encoding='utf8') as file:
            content: dict = DefaultMunch.fromDict(yaml.safe_load(file))

    exercises = []

    # select topic by chance
    topics_selected = choice(list(config.topics.keys()), size=config.batch_size)

    # select topic-levels by chance
    selection: list = []

    for topic in topics_selected:
        # content contains q1, q2, q3, ex1, ex2, ...
        counter = 0
        while True:
            topic_level: str = str(
                    choice(
                        candidate_levels_per_topic(
                            config.topics[topic].max_level,
                            topic,
                            content
                            ),
                        1
                    )[0]
                )

            topic_level: str = topic + "." + topic_level

            counter += 1

            # only select topic-level if that topic-level is not in cache of
            # previously submitted exercises
            if (topic_level not in config.past_exercises and
                topic_level not in selection):
                selection.append(topic_level)
                break

            if counter == (3+1):
                # safety break for infinite while loop, max. 3 retries
                # it could be that all levels of some topic are already in the past_exercises list.  in that case we just select the current level and don't worry about not wanting to resend exercises with the same topic and level twice within a certain time frame.
                selection.append(topic_level)
                break

    # update list of past exercises in config
    with open(config.self, 'w') as file:
        for item in selection:
            config.past_exercises.append(item)
            if len(config.past_exercises) >= 3:
                    config.past_exercises.pop(0)
        del config["self"]
        yaml.safe_dump(config, file, sort_keys=False)
        logging.info("Cached exercise in config.")

    # instantiate exercises
    out = []
    for sel in selection:
        t = sel.split(".")[0]
        x = sel.split(".")[1]
        # content = DefaultMunch.fromDict(yaml.safe_load(file))
        full_ex: dict = content[t][x]
        full_ex["topic"] = t.capitalize()
        inst_ex = instantiate_exercise(full_ex)
        out.append(inst_ex)

    return(out)