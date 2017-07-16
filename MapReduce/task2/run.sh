hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar  \
-input/user/$USER/task1total \
-output /user/$USER/task2total \
-mapper mapper.py  \
-file mapper.py  \
-reducer reducer.py \
-file reducer.py
