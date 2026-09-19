import json


def extract_text(text_entities: list[dict]):
    res = ""
    for entity in text_entities:
        res += entity["text"]
    return res


def load_messages_from_telegram(path: str):
    with open(path, "r", encoding="utf-8") as f:
        chat = json.load(f)
        messages = chat["messages"]
        only_messages = list(filter(lambda x: x['type'] == "message" and x.get('forwarded_from', None) is None, messages))
    clear_chat = []
    for m in only_messages:
        message_text = extract_text(m['text_entities'])
        if message_text:
            clear_chat.append({
                "id": m['id'],
                "date": m["date"],
                "date_unixtime": m["date_unixtime"],
                "from_id": m['from_id'],
                "text": message_text
            })
    return clear_chat

