import logging
import yaml
from pathlib import Path
from munch import DefaultMunch 
from numpy.random import choice
from numpy import array
from .instantiate_exercise import instantiate_exercise

def fetch_exercises(config):

    topics = config.topics.keys()
    with open(Path().cwd() / "exercises" / "exercises_general.yaml",'r',encoding='utf8') as file:
            content = DefaultMunch.fromDict(yaml.safe_load(file))
    for topic in topics:
        # content contains q1, q2, q3, ex1, ex2, ...
        levels = []
        levels.append(list(content.keys()))

        selection = []
        for topic in topics:
            counter = 0
            while True:
                topic_level = str(
                     choice(
                          array(
                               list(
                                    content[topic].keys()
                                    )
                                ),
                            1
                        )[0]
                    )
                topic_level = topic + "." + topic_level
                counter += 1
                if topic_level not in config.past_exercises:
                    selection.append(topic_level)
                    break
                if counter == 10:
                    # REVIEW:
                    # in case of some exercise topic all levels have been used within the last few runs
                    selection.append(topic_level)
                    break

    with open(config.self, 'w') as file:
        for item in selection:
            config.past_exercises.append(item)
            if len(config.past_exercises) >= 3:
                    config.past_exercises.pop(0)
        del config["self"]
        yaml.safe_dump(config, file)
        logging.info("Cached exercise in config.")
    
    out = []
    for sel in selection:
        t = sel.split(".")[0]
        x = sel.split(".")[1]
        # content = DefaultMunch.fromDict(yaml.safe_load(file))
        full_ex = content[t][x]
        full_ex["topic"] = t.capitalize()
        inst_ex = instantiate_exercise(full_ex)
        out.append(inst_ex)

    return(out)

# ================= OLD =================
# def fetch_exercises(config):

#     exercises = {}
#     for topic in config.exercises.keys():
#             with open(Path().cwd() / "exercises" / f"{topic}.yaml",'r',encoding='utf8') as file:
#                 content = DefaultMunch.fromDict(yaml.safe_load(file))
#                 # content contains q1, q2, q3, ex1, ex2, ...
#             exercises[topic] = list(content.keys())

#     selection = []
#     for topic in exercises.keys():
#         while True:
#             topic_ex = str(choice(exercises[topic], 1)[0])
#             if topic_ex not in config.past_exercises:
#                 selection.append(topic + "." + topic_ex)
#                 break

#     with open(config.self, 'w') as file:
#         for item in selection:
#             config.past_exercises.append(item)
#             if len(config.past_exercises) >= 3:
#                     config.past_exercises.pop(0)
#         del config["self"]
#         yaml.safe_dump(config, file)
#         logging.info("Cached exercise in config.")
    
#     out = []
#     for sel in selection:
#         t = sel.split(".")[0]
#         x = sel.split(".")[1]
#         with open(
#              Path().cwd() / "exercises" / f"{t}.yaml",'r', encoding='utf8') as file:
#             content = DefaultMunch.fromDict(yaml.safe_load(file))
#             full_ex = content[x]
#             full_ex["topic"] = t
#             out.append(full_ex)
    


#     return(out)


#     # return(content.)