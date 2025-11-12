import random
from typing import List, Dict, Tuple

# Constants from objectsData_en
FEW_OBJECTS = [
    ("Broom", 1), ("Clock", 1), ("Clothes tree", 1),
    ("Trash can", 1), ("Kettle", 1), ("Lamp", 1),
    ("Newspaper", 1), ("Notebook", 1), ("Poster", 1),
    ("Rug", 1), ("Sofa", 1), ("Tissue", 1),
    ("Tray", 1), ("TV", 1), ("Waste paper ball", 1),
    ("Clothes hangers", 2), ("Desk", 2), ("Paintings", 2),
    ("Pen", 1), ("Pillow", 2), ("Potted plants", 1),
    ("Bowl", 4), ("Chair", 4), ("Cup", 2), ("Book", 5)
]

MANY_OBJECTS = [
    ("Basketball", 1), ("Chess board&pieces", 1), ("Dice", 1),
    ("Kalimba", 1), ("Tennis ball", 1), ("Treadmill", 1),
    ("Building block", 5), ("Broom", 1), ("Clock", 1),
    ("Clothes tree", 1), ("Trash can", 1), ("Kettle", 1),
    ("Lamp", 1), ("Newspaper", 1), ("Notebook", 1),
    ("Poster", 1), ("Rug", 1), ("Sofa", 1),
    ("Tissue", 1), ("Tray", 1), ("TV", 1),
    ("Waste paper ball", 1), ("Clothes hangers", 2), ("Desk", 2),
    ("Paintings", 2), ("Pen", 1), ("Pillow", 2),
    ("Potted plants", 1), ("Bowl", 4), ("Chair", 4),
    ("Cup", 2), ("Book", 5)
]

HUMAN_OBJECTS = [("Other people", 1)]
DUMMY_OBJECTS = [("Dummy", 1)]

class SceneSettings:
    def __init__(self, objects: List[Tuple[str, int]], agent_type: List[Tuple[str, int]]):
        self.items = self._create_items_list(objects, agent_type)
        random.shuffle(self.items)

    def _create_items_list(self, objects: List[Tuple[str, int]], 
                          agent_type: List[Tuple[str, int]]) -> List[Dict]:
        items = []
        # Add all objects
        for name, count in objects:
            items.append((name, count))
        # Add agent type (human/dummy)
        for name, count in agent_type:
            items.append((name, count))
        return items

def get_all_scene_settings() -> Dict[str, SceneSettings]:
    return {
        "few_dummy": SceneSettings(FEW_OBJECTS, DUMMY_OBJECTS).items,
        "few_human": SceneSettings(FEW_OBJECTS, HUMAN_OBJECTS).items,
        "many_dummy": SceneSettings(MANY_OBJECTS, DUMMY_OBJECTS).items,
        "many_human": SceneSettings(MANY_OBJECTS, HUMAN_OBJECTS).items,
    }

# 对齐 key 的索引名称
def get_all_scene_settings_align() -> Dict[str, SceneSettings]:
    return {
        "dummy_few": SceneSettings(FEW_OBJECTS, DUMMY_OBJECTS).items,
        "human_few": SceneSettings(FEW_OBJECTS, HUMAN_OBJECTS).items,
        "dummy_many": SceneSettings(MANY_OBJECTS, DUMMY_OBJECTS).items,
        "human_many": SceneSettings(MANY_OBJECTS, HUMAN_OBJECTS).items,
    }

if __name__ == "__main__":
    settings = get_all_scene_settings()
    print(settings["few_dummy"], len(settings["few_dummy"]))
    print(settings["few_human"], len(settings["few_human"]))
    print(settings["many_dummy"], len(settings["many_dummy"]))
    print(settings["many_human"], len(settings["many_human"]))
