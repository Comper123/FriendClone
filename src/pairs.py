def group_turns(chat):
    if len(chat) == 0: return []
    
    old_from_id = chat[0]["from_id"]
    turns = [{"from_id": old_from_id, "text": chat[0]["text"]}]
    
    for i in range(1, len(chat)):
        if chat[i]["from_id"] == old_from_id:
            turns[-1]["text"] += ("\n" + chat[i]["text"])
        else:
            old_from_id = chat[i]['from_id']
            turns.append({"from_id": old_from_id, "text": chat[i]["text"]})
    
    return turns
            

def build_pairs(turns, friend_id, context_size):
    pairs = []
    for i, turn in enumerate(turns):
        if turn['from_id'] == friend_id:
            start = max(0, i - context_size)
            context = turns[start:i]
            pairs.append({"context": context, "reply": turn["text"]})
    return pairs


def format_pair(pair, friend_id):
    prompt = []
    for item in pair["context"]:
        msg = "он: " if item["from_id"] == friend_id else "я: "
        msg += item["text"]
        prompt.append(msg)
    return "\n".join(prompt), pair["reply"]