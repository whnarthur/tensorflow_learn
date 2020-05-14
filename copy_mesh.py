import os
import sys

if __name__ == "__main__":
    city = sys.argv[1]
    path = '/data1/coco/mre_docker/waibao/3_res/'
    dst_path = '/data1/coco/mre_docker/waibao/' + city
    with open("/data1/coco/mre_docker/waibao/%s.txt" % city) as fp:
        for line in fp.readlines():
            if len(line) < 5:
                continue
            dir_path = line[:4]
            fullpath = path + dir_path + "/" + line.strip()
            print(fullpath)

            os.system("cp -rf %s %s" % (fullpath, dst_path))
