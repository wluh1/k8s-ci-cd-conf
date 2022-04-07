import yaml
import os

with open("./values.yaml") as f:
    y = yaml.safe_load(f)
    old_tag = y["images"]["tag"]
    s = old_tag.split(".")
    s[-1] = str(int(s[-1]) + 1)
    new_tag = ".".join(s)
    y["images"]["tag"] = new_tag

with open("modified.yaml", "w") as ostream:
    yaml.dump(y, ostream, default_flow_style=False, sort_keys=False)

os.remove("values.yaml")
os.rename("modified.yaml", "values.yaml")
