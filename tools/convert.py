import os


def replace_row():
    for foldName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.json'):
                filename_a = os.path.splitext(filename)[0]
                f = open(os.path.join(foldName, filename), "r")
                data = f.read()
                data_a = data.replace("\"type\": \"minecraft:crafting_shapeless\",",
                                      "  \"format_version\": \"1.12\",\n\"minecraft:recipe_shapeless\": {\n\"description\": {\n\"identifier\": \"" + filename_a + "\"},")
                data_b = data_a.replace("\"type\": \"minecraft:crafting_shaped\",",
                                      "  \"format_version\": \"1.12\",\n\"minecraft:recipe_shaped\": {\n\"description\": {\n\"identifier\": \"" + filename_a + "\"},")
                with open(os.path.join(foldName, filename), 'w') as f:
                    f.write(data_b)
                    print(os.path.join(foldName, filename),
                          'converted successfully.')


if __name__ == '__main__':
    path = input("Path:")
    replace_row()
