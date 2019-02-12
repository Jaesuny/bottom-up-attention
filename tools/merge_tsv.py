import csv
import sys

csv.field_size_limit(sys.maxsize)

def merge_tsvs():
    FIELDNAMES = ['image_id', 'image_w','image_h','num_boxes', 'boxes', 'features']
    test = ['data/vg_resnet101_faster_rcnn_genome.tsv.%d' % i for i in range(8)]

    outfile = 'data/merged.tsv'
    with open(outfile, 'ab') as tsvfile:
        writer = csv.DictWriter(tsvfile, delimiter = '\t', fieldnames = FIELDNAMES)   
        
        for infile in test:
            with open(infile) as tsv_in_file:
                reader = csv.DictReader(tsv_in_file, delimiter='\t', fieldnames = FIELDNAMES)
                for item in reader:
                    try:
                        writer.writerow(item)
                    except Exception as e:
                        print e                           

merge_tsvs()
