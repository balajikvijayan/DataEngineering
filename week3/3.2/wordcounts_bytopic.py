from mrjob.job import MRJob
from string import punctuation
import os

class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        for word in line.split():
            yield ((os.environ['map_input_file'].split('\\')[1], word.strip(punctuation).lower()), 1)

	# def combiner(self, (topic, word), counts):
		# yield (topic,word), sum(counts)
			
    def reducer(self, (topic, word), counts):
        yield (topic+'_'+word), sum(counts)

if __name__ == '__main__':
    MRWordFreqCount.run()