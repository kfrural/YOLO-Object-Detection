import json
import os

def convert_labelme_to_yolo(json_dir, output_dir):
    for json_file in os.listdir(json_dir):
        if not json_file.endswith('.json'):
            continue

        with open(os.path.join(json_dir, json_file), 'r') as f:
            data = json.load(f)
            height = data['imageHeight']
            width = data['imageWidth']

            output_path = os.path.join(output_dir, json_file.replace('.json', '.txt'))
            with open(output_path, 'w') as out:
                for shape in data['shapes']:
                    label = shape['label']
                    x_min, y_min = shape['points'][0]
                    x_max, y_max = shape['points'][1]

                    x_center = (x_min + x_max) / 2 / width
                    y_center = (y_min + y_max) / 2 / height
                    obj_width = (x_max - x_min) / width
                    obj_height = (y_max - y_min) / height

                    out.write(f"{label} {x_center} {y_center} {obj_width} {obj_height}\n")

if __name__ == "__main__":
    convert_labelme_to_yolo('data/labels/json/', 'data/labels/train/')
