import os
import shutil
import sys

def copy_files(input_dir, output_dir):
    if not os.path.exists(input_dir):
        return
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    name_count={}
    for root, i, files in os.walk(input_dir):
        for file in files:
            original_path = os.path.join(root,file)
            base_name, ext = os.path.splitext(file)
            if file not in name_count:
                name_count[file]=1
                new_name=file
            else:
                name_count[file]+=1
                new_name = f"{base_name}{name_count[file]-1}{ext}"
            target_path = os.path.join(output_dir, new_name)
            shutil.copy(original_path, target_path)

input_dir=sys.argv[1]
output_dir=sys.argv[2]
copy_files(input_dir, output_dir)