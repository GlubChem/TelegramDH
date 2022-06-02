from typing import List, Dict

def fix_names(messages : List[List[Dict[str, str]]]) -> List[List[Dict[str, str]]]:
    messages = [
        [
            {'ent' : entity['ent'].lower(), 'type' : entity['type']}
            for entity in message
            ]
        for message in messages
        ]
    return messages