import json
import os
import shutil


# Assumptions -
#   1. Root directory is the directory where the script is being run

root_dir = os.getcwd()
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file == 'version.json':
            print(f'Updating version at : {os.path.join(subdir, file)}')
            with open(os.path.join(subdir, file), "r+") as f:
                version_json = json.loads(f.read())
                version_json['version'] += 1
                f.seek(0)
                f.truncate()
                f.write(json.dumps(version_json))
                f.close()
print("creating archive file at :"+ root_dir)
shutil.make_archive('coding_challenge_isg_'+str(version_json['version']), 'zip', root_dir='.')