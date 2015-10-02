import boto
from collections import Counter

# Connect to S3
access_key = 'AKIAJ7CE4VJI5K4QGEEA'
access_secret_key = '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'
conn = boto.connect_s3(access_key, access_secret_key)

bucket_name = 'dataengineering'
b = conn.get_bucket(bucket_name)
text = b.get_key('shakespeare-sonnets.txt').get_contents_as_string().replace('\n','')

word_freq = Counter(text.split()).most_common()

newbucket = 'dataengineering1'
if conn.lookup(newbucket) is None:
    b = conn.create_bucket(newbucket, policy='public-read')
else:
    b = conn.get_bucket(newbucket)

file_object = b.new_key('word_freq.txt')
file_object.set_contents_from_string(str(word_freq).strip('[]'),
                                     policy='public-read')