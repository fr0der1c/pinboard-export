from typing import Dict, List, Union

import pinboard
from nebooman import Manager

pinboard_key = ""

pb = pinboard.Pinboard(pinboard_key)

tags: List = pb.tags.get()
tags.sort(key=lambda t: len(t.name))  # sort by length

print("tags: {}".format(tags))

bookmarks = []


def get_key(parent: Union[Dict, List], key: str):
    """simulate `dict.get()` on list"""
    if isinstance(parent, dict):
        lst = parent["children"]
    else:
        lst = parent

    for each in lst:
        if each["title"] == key and "href" not in each:
            return each

    item = {"title"   : key,
            "children": []}
    print("Create parent folder {}".format(key))

    if isinstance(parent, dict):
        parent["children"].append(item)
    else:
        parent.append(item)

    return item


for tag in tags:
    print("Processing tag {}".format(tag))
    posts = [{"href": b.url, "title": b.description} for b in pb.posts.all(tag=[tag.name])]

    if tag.name.find("/") == -1:
        bookmarks.append({"title"   : tag.name,
                          "children": posts})
        print("Add top level tag {} and its {} posts".format(tag.name, tag.count))
    else:
        splitted = tag.name.split("/")
        parent = bookmarks

        for folder_name in splitted[:len(splitted) - 1]:
            parent = get_key(parent, folder_name)

        parent["children"].append({"title"   : splitted[-1],
                                   "children": posts})
        print("Add tag {} and its {} posts".format(tag.name, tag.count))

bookmarks = [{"title"   : "Pinboard",
              "children": bookmarks}]  # add top level folder
print(bookmarks)

# save to file
manager = Manager()
manager.bookmarks = bookmarks
with open("pinboard.html", "w") as f:
    manager.write_bookmarks_file(f)
