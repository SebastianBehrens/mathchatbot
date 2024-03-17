def yield_exercise_tex(type, topic, instruction, math):

    lat_newline = r"\\"
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