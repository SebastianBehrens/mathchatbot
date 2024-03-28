import logging
# TODO: handle errors per notification
# from send_message_telegram send_message_telegram
def yield_exercise_tex(
        type: str,
        topic: str,
        instruction: str,
        math:str) -> str:

    lat_newline = r"\\"
    print("\n\n\n")
    print(topic)
    print("\n\n\n")
    if topic.lower() == "exponents":
        topic = "Exponenten"
    elif topic.lower() == "fractions":
        topic = "Brüche"
    elif topic.lower() == "roots":
        topic = "Wurzeln"
    elif topic.lower() == "parentheses":
        topic = "Klammern"
    else:
        logging.error("topic not yet translated.")
        # send_message_telegram


    tex_template = (
        r"\documentclass[preview]{standalone}"
        r"\usepackage{tcolorbox}"
        r"\tcbuselibrary{theorems}"
        f"\\newtcbtheorem[number within=section]{{mytheo}}{{{type}}}"

        r"{colback=green!5,colframe=green!35!black,fonttitle=\bfseries}{th}"
        r"\begin{document}"
        r"\begin{mytheo*}"
        f"{{{topic.capitalize()}}}"
        f"{{{instruction}:"
        f"{math}}}"
        r"\end{mytheo*}"
        r"\end{document}"
    )

    return (tex_template)