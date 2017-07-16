hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapred.reduce.tasks=1 \
-input /data/assignments/ex2/part2/stackLarge.txt \
-output /user/$USER/1112 \
-mapper mapper1.py \
-file mapper1.py \
-reducer reducer1.py \
-file reducer1.py \

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapred.reduce.tasks=1 \
-input /user/$USER/1112 \
-output /user/$USER/assignment2/task4 \
-mapper mapper2.py \
-file mapper2.py \
-reducer reducer2.py \
-file reducer2.py 
