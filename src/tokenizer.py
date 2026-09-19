def build_vocab(texts):
    """Составляем словарь (токенизатор)"""
    chars = set()
    for text in texts:
        chars.update(text)
    chars = sorted(chars)
    stoi = {s: i for i, s in enumerate(chars)}
    itos = {i: s for i, s in enumerate(chars)}
    sep_id = len(chars)
    end_id = len(chars) + 1
    return stoi, itos, sep_id, end_id

   
def encode_pair(prompt, reply, stoi, sep_id, eos_id):
    prompt_ids = [stoi[s] for s in prompt]
    reply_ids = [stoi[s] for s in reply]
    
    ids = prompt_ids + [sep_id] + reply_ids + [eos_id]
    # Место где начинается маска
    n_masked = len(prompt_ids) + 1
    labels = [-100 if i < n_masked else ind for i, ind in enumerate(ids)]
    return ids, labels