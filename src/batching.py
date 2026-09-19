import torch


def make_xy(ids, labels):
    x = ids[:-1]
    y = labels[1:]
    return x, y
    
    
def collate(batch):
    max_len = max(len(x) for x, y in batch)
    xs, ys = [], []
    for x, y in batch:
        pad = max_len - len(x)
        xs.append(x + [0] * pad)
        ys.append(y + [-100] * pad)
    return (torch.tensor(xs, dtype=torch.long),
            torch.tensor(ys, dtype=torch.long))