hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapred.reduce.tasks=1 \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D mapred.text.key.comparator.options=-nr \
-input /user/$USER/task4total \
-output /user/$USER/task5total \
-mapper mapper.py \
-file mapper.py \
-reducer reducer.py \
-file reducer.py 
