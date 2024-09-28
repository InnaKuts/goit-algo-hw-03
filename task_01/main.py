import os
import shutil
import sys


def copy_files(src: str, dst: str):
    if not os.path.isdir(src):
        raise Exception(f'Directory doesn\'t exist: `{src}`')
    os.makedirs(dst, exist_ok=True)
    for name in os.listdir(src):
        path = os.path.join(src, name)
        if os.path.isdir(path):
            dst_root = os.path.join(dst, name)
            copy_files(path, dst_root)
        else:
            ext = os.path.splitext(name)[1][1:]
            dst_root = os.path.join(dst, ext)
            dst_path = os.path.join(dst_root, name)
            os.makedirs(dst_root, exist_ok=True)
            shutil.copy(path, dst_path)


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print(f'Please, provide a source and destination')
        return
    args.append('dest')

    copy_files(args[0], args[1])


if __name__ == '__main__':
    main()
