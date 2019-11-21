import pandas as pd
import re
import urllib.request as req

# text | regex
# Lucina, Heiress to the Exalt"s Blood | (([a-zA-Z]+), ([\S ]+))
# Lucina | (([a-zA-Z]+)(!, [a-zA-Z ]+))
# Lucina 1 or Lucina 4(3) | (([a-zA-Z]+) ([0-9]{1}(\([0-9X]\))?))
# Lucina B01 | (([a-zA-Z]+) ([a-zA-Z][0-9]{2}))


patterns = {
          "full": r"(([\S ^,^\d]+), ([\S ]+))",           # Lucina, Heiress to the Exalt's Blood
          "name": r"^([\S ^,^\d]+)$",                     # Lucina
          "cost": r"(([\S ^,^\d]+) (\d(\([\dX]\))?))",    # Lucina 1 or Lucina 4(3)
          "set":  r"(([\S ^,^\d]+) ([BPS]\d{2}))",        # Lucina B01
          }

data_url = "https://dl.dropboxusercontent.com/s/xe9iwnh806uonnf/carddata.txt"
data_tsv = "data/carddata.txt"
data_json = "data/carddata.json"

def load_data():
    try:
        req.urlretrieve(data_url, data_tsv)
        df_temp = pd.read_csv(data_tsv, sep="\t")
        print("downloaded tsv")
        df_temp.to_json(data_json)
    finally:
        df = pd.read_json(data_json)
        print("read json")
    return df

# todo: make this work with more than one query at a time... or don't we'll see
def parse_query(query, df):
    query = query.strip().lower()
    full = re.search(patterns["full"], query, flags=re.I)
    name = re.search(patterns["name"], query, flags=re.I)
    cost = re.search(patterns["cost"], query, flags=re.I)
    set = re.search(patterns["set"], query, flags=re.I)

    if (full):
        full_val = re.escape(full.group(1))
        full_frame = val_matches_exact(full_val, df, "Name")
        if full_frame.empty:
            full_frame = val_matches(full_val, df, "Name")
        return full_frame
    elif (cost):
        name_val = re.escape(cost.group(2))
        cost_val = re.escape(cost.group(3))
        df = val_matches(name_val, df, "Name")
        return val_matches_exact(cost_val, df, "Cost")
    elif (set):
        name_val = re.escape(set.group(2))
        set_val = re.escape(set.group(3))
        df = val_matches(name_val, df, "Name")
        return val_matches_exact(set_val, df, "Set")
    elif (name):
        name_val = re.escape(name.group(1))
        return val_matches(name_val, df, "Name")
    else:
        return pd.DataFrame() # return an empty dataframe if no match

def val_matches(val, df, col):
    return df[df[col].str.match(val, na=False, flags=re.I)]

def val_matches_exact(val, df, col):
    return df[df[col].str.match("^" + val + "$", na=False, flags=re.I)]

if __name__ == "__main__":
    cd = load_data()
    print(cd)
    cd["Cost"] = cd["Cost"].astype(str) # this is needed to make single number costs work, apparently. unsure why.
    a = input("Input query: ")
    res = parse_query(a, cd)
    if len(res.index) == 1:
        print(res.iloc[0]["Name"])
    elif res.empty:
        print("No result!")
    else:
        print(res)
