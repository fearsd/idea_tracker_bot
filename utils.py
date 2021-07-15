"""This module contains some extra functions."""

def ideas_to_text(ideas):
    """
    Idaeas to text to send.

    Parameters:
        ideas: List of ideas.

    Returns:
        message: Result message.
    """
    message = ''

    for idea in ideas:
        message += '{}\n{}\n\n'.format(idea.date_created.isoformat(), idea.body)
    return message
