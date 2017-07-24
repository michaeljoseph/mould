import io
import os


def write_directory(directory_entries, target_directory):
    for directory_entry in directory_entries:
        dir_to_create = os.path.join(target_directory, directory_entry['path'])
        print('creating {}'.format(dir_to_create))

        if not os.path.exists(dir_to_create):
            os.mkdir(dir_to_create)

        for file_entry in directory_entry['files']:
            file_to_create = os.path.join(target_directory, file_entry['path'])
            print('writing {}'.format(file_to_create))

            mode = 'w{}'.format('b' if file_entry['binary'] else 't')
            with io.open(file_to_create, mode=mode) as fh:
                fh.write(file_entry['content'])
