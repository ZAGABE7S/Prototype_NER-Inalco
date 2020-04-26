import subprocess
subprocess_output_dict = {
        "pipe": subprocess.PIPE,
        "stdout": subprocess.STDOUT,
        "devnull": subprocess.DEVNULL,
    }

cmd = ['/usr/lib/jvm/java-8-oracle/bin/java', '-mx1000m', '-cp', '/home/jc-zagabe/Documents/preproc_data/lib/postagger/stanford-postagger.jar', 'edu.stanford.nlp.tagger.maxent.MaxentTagger', '-model', '/home/jc-zagabe/Documents/preproc_data/lib/postagger/models/french.tagger', '-textFile', '/tmp/tmpw9grzlw2', '-tokenize', 'false', '-outputFormatOptions', 'keepEmptySentences', '-encoding', 'utf8']
PIPE = -1
STDOUT = -2
DEVNULL = -3
p = subprocess.Popen(cmd,stdin=PIPE,stdout=STDOUT,stderr=PIPE)

(stdout, stderr) = p.communicate()

print(stdout)