def candidate_levels_per_topic(max_level, topic, content):
    levels = list(content[topic].keys())
    if max_level == 'all':
        candidate_levels = levels
    else:
        candidate_levels = levels[0:max_level]

    return(candidate_levels)