import os
import json
from collections import defaultdict

def count_ids_in_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return len([item for item in data if 'id' in item])
            elif isinstance(data, dict):
                return len([k for k in data if 'id' in data[k]])
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return 0

def scan_directory(root_dir):
    stats = defaultdict(lambda: defaultdict(int))
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.json'):
                reasoning_type = filename.replace('.json', '')
                full_path = os.path.join(dirpath, filename)
                folder_key = os.path.relpath(dirpath, root_dir)
                count = count_ids_in_json(full_path)
                stats[folder_key][reasoning_type] += count
    return stats

# 用法示例
root_folder = "OpenRBench"  # 替换为你的根目录路径
results = scan_directory(root_folder)

# 输出结果
for folder, types in results.items():
    print(f"\nFolder: {folder}")
    for reasoning_type, count in types.items():
        print(f"  {reasoning_type}: {count}")
