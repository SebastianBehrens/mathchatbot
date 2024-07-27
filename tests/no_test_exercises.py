import unittest
import logging
import requests
import urllib
from pathlib import Path
from scripts.yield_exercise_tex import yield_exercise_tex
from scripts.instantiate_exercise import instantiate_exercise
from scripts.tex_to_pdf import tex_to_pdf
from munch import DefaultMunch
import yaml

class ExerciseTest(unittest.TestCase):

    def test_variables_in_exercises(self):
        with open(Path().cwd() / "exercises" / "exercises_general_levels.yaml",'r',encoding='utf8') as file:
                content: dict = DefaultMunch.fromDict(yaml.safe_load(file))
        for topic in content.keys():
            for level in content[topic]:
                exercise = content[topic][level]
                self.assertEqual('foo'.upper(), 'FOO')
                exercise["topic"] = topic.capitalize()
                exercise = instantiate_exercise(exercise)
                tex = yield_exercise_tex(
                        type=exercise.type,
                        topic=exercise.topic,
                        instruction=exercise.instruction,
                        math=exercise.math)

                tex_str_enc: urllib = urllib.parse.quote(tex, safe='')
                url: str = f"https://latexonline.cc/compile?text={tex_str_enc}"
                response: requests = requests.get(url = url, timeout = 5)
                if response.status_code == 400:
                    logging.error(f"Topic: {topic}")
                    logging.error(f"Level: {level}")
                    logging.error(response.status_code)
                    logging.error(response.text)
                self.assertNotEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
