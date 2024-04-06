import logging
# TODO: handle errors per notification
# from send_message_telegram send_message_telegram
def yield_exercise_tex(
        type: str = "",
        topic: str = "",
        instruction: str = "",
        math:str = "") -> str:

    if type is None:
        type = ""
    if topic is None:
        topic = ""
    if instruction is None:
        raise  Exception("Topic supplied to yield_exercise_tex is none.")
    if math is None:
        math = ""

    lat_newline = r"\\"



    tex_template = (
    r"""
    \documentclass{standalone}
    \usepackage{amsmath}
    \usepackage[utf8]{inputenc} % to compile umlaute
    \usepackage[breakable,skins]{tcolorbox}
    \usepackage{xcolor}
    \newtcolorbox{mybox}[1]{
    before skip=1ex,
    after skip=1ex,
    top=2.5ex,
    bottom=2.5ex,
    width=18em,
    breakable, 
    enhanced,
    coltitle=black,
    colback=white,
    sharp corners,
    title={#1},
    attach boxed title to top left={
        yshift=-\tcboxedtitleheight,
        xshift=\tcboxedtitleheight
        },
    boxed title style={
        size=small,
        colback=white,
        sharp corners
        }
    }

    \begin{document}
    \begin{mybox}
    """
    f"{{{topic.capitalize()}}}"
    r"\vspace{1.25em}"
    f"{instruction}"
    f"{math}"
    """
    \end{mybox}
    \end{document}
    """
    )

    return (tex_template)
