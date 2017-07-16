hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapred.reduce.tasks=1 \
-input /data/assignments/ex1/uniLarge.txt \
-output /user/$USER/task7total \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py





