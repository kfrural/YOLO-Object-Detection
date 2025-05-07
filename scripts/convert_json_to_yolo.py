import json
import os

def convert_json_to_yolo(json_path, txt_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    width = data['imageWidth']
    height = data['imageHeight']
    
    objects = []
    for shape in data['shapes']:
        label = shape['label']
        points = shape['points']
        
        x_min = min(p[0] for p in points)
        y_min = min(p[1] for p in points)
        x_max = max(p[0] for p in points)
        y_max = max(p[1] for p in points)
        
        x_center = ((x_min + x_max) / 2) / width
        y_center = ((y_min + y_max) / 2) / height
        w = (x_max - x_min) / width
        h = (y_max - y_min) / height
        
        class_index = 0
        
        obj_line = f"{class_index} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n"
        objects.append(obj_line)
    
    with open(txt_path, 'w') as f:
        f.writelines(objects)

def main():
    json_dir = 'path/to/json/files'
    txt_dir = 'path/to/txt/files'
    
    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):
            json_path = os.path.join(json_dir, filename)
            txt_path = os.path.join(txt_dir, filename.replace('.json', '.txt'))
            convert_json_to_yolo(json_path, txt_path)

if __name__ == '__main__':
    main()