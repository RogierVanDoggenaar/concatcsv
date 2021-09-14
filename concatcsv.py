import sys
import time


def append(input_file:str, output_file:str, first_line:bool):
    print('now processing %s' % input_file)
    cnt = 0
    with open(input_file, "r") as f:
        if not first_line:
            f.readline().rstrip()
        with open(output_file, "a") as of:
            while True:
                line = f.readline().rstrip()
                if not line:
                    break

                of.write(line+'\n')
                cnt += 1
                if cnt % 1000 == 0:
                    print('processed %d lines...' % cnt)
            of.close()
        f.close()
    print('done processing %d lines in %s' % (cnt, input_file))


if __name__ == '__main__':
    outp_file = sys.argv[-1]
    inp_files = sys.argv[1:-1]
    print('input files to process: ', inp_files)
    print('appending to: %s' % outp_file)
    started = time.time()
    print('Started %s' % time.strftime('%Y-%m-%d %A %H:%M:%S GMT', time.localtime()))
    process_first = True
    for inp_file in inp_files:
        append(input_file=inp_file, output_file=outp_file, first_line=process_first)
        process_first = False  # only include first line once
    finished = time.time()
    print('Finished %s' % time.strftime('%Y-%m-%d %A %H:%M:%S GMT', time.localtime()))
    print('It took: %s seconds' % round(finished - started, 4))
